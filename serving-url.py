#!/usr/bin/env python

import sys
import json
import logging
import webapp2
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.cloud import storage

# from https://stackoverflow.com/a/54356031/599991
from requests_toolbelt.adapters import appengine
appengine.monkeypatch()


class ServingUrl(webapp2.RequestHandler):
    def post(self):
        logging.debug('request with input: %s' % self.request.body)

        if self.request.body:
            input = json.loads(self.request.body)
            filename = input["name"]
            bucket = input["bucket"]

            if bucket and filename:
                blobkey = blobstore.create_gs_key(
                    '/gs/' + bucket + '/' + filename)

                if blobkey:
                    url = None
                    error = None

                    try:
                        url = images.get_serving_url(blobkey, secure_url=True)
                    except Exception as e:
                        error = e
                    finally:
                        blob = storage.Client().get_bucket(bucket).get_blob(filename)
                        metadata = dict(blob.metadata or {})

                        if url:
                            logging.debug('url generated: %s' % url)
                            metadata['url'] = url
                        if error:
                            metadata['error'] = str(
                                error) or error.__doc__ or error

                        blob.metadata = metadata
                        blob.patch()

                        if error:
                            raise error

                    return self.response.write(url)

            raise Exception('image cannot be found')
        else:
            raise Exception('invalid request')

        self.error(404)


app = webapp2.WSGIApplication([('/serve', ServingUrl)], debug=True)

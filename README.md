**Disclaimer 1**: This solution is based on the App Engine's Python 2 environment. There are [plans to replace it by something more modern](https://github.com/albertcht/python-gcs-image/issues/3).

**Disclaimer 2**: There are alternative implementations of this same solution that seem to be better maintained. Please consider taking a look at [albertcht/python-gcs-image](https://github.com/albertcht/python-gcs-image).

---


App Engine provides the ability to manipulate image data using a dedicated Images service. The Images service can manipulate images, composite multiple images into a single image, convert image formats, provide image metadata such as format, width, height, and a histogram of color values.


# [get_serving_url()](https://cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.api.images#google.appengine.api.images.get_serving_url)

> **⚠️ Please note**: even though the image will be served completely independent from our app, we can only generate the url we need from within Google's App Engine. It's the only fucking way! Once we have the URL, we can serve the images and manipulate them as we want...

Obtains a URL that will serve the underlying image.

This URL is served by a high-performance dynamic image serving infrastructure. As the image is served independently from your app, it does not generate load and can be highly cost effective. The URL returned by this method is always publicly accessible but not guessable.

The method returns a URL encoded with the specified size and crop arguments allowing dynamic resizing and cropping with certain restrictions. If you do not specify any arguments, the method returns the default URL for the image. To dynamically resize and crop, specify size and crop arguments, or simply append options to the end of the default URL obtained via this call.

Example:

```haskell
get_serving_url -> "http://lh3.ggpht.com/SomeCharactersGoesHere"
```
To get a 32-pixel-sized version (aspect-ratio preserved), append `=s32` to the URL:

```haskell
http://lh3.ggpht.com/SomeCharactersGoesHere=s32
```
To get a 32-pixel cropped version, append `=s32-c`:

```haskell
http://lh3.ggpht.com/SomeCharactersGoesHere=s32-c
```
Available sizes are any integer in the range **`[0, 3200]`** and is available as [IMG_SERVING_SIZES_LIMIT](https://github.com/GoogleCloudPlatform/python-compat-runtime/blob/743ade7e1350c790c4aaa48dd2c0893d06d80cee/appengine-compat/exported_appengine_sdk/google/appengine/api/images/__init__.py#L1798).

Parameters
* `blob_key` – The BlobKey, BlobInfo, string, or Unicode representation of BlobKey of the blob whose URL you require.

* `size` – Integer of the size of resulting images.

* `crop` – Boolean value. True requests a cropped image, while False requests a resized image.

* `secure_url` – Boolean value. True requests a https URL, while False requests a http URL.

* `filename` – The file name of a Google Storage object whose URL you require.

* `rpc` – Optional UserRPC object.

Returns
A URL string.

There are [many more parameters that can be used](https://stackoverflow.com/a/25438197/599991), but they are not officially supported.

## References

* https://medium.com/google-cloud/uploading-resizing-and-serving-images-with-google-cloud-platform-ca9631a2c556

* https://cloud.google.com/appengine/docs/standard/python/images/#get-serving-url

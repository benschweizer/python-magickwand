python-magickwand
=================
These are Python bindings for the ImageMagick [MagickWand C-API](http://www.imagemagick.org/api/magick-wand.php).

Examples
========
convert
-------
``` python
from magickwand.image import Image
image = Image('favicon.ico')
image.convert(size=(16,16),depth=8)
image.save('favicon.png')
```

flip
----
``` python
from magickwand.image import Image
image = Image('foo.jpg')
image.format = 'PNG'
image.flip()
image.save('flip.png')
```

Compatibility
=============
API Versions
------------
The MagickWand API is available in various versions:

<table>
<tr><td>ImageMagick</td><td>MagickWand</td><td>Status</td></tr>
<tr><td>6.4</td><td>1</td><td>unknown</td></tr>
<tr><td>6.5</td><td>2</td><td>supported</td></tr>
<tr><td>6.6</td><td>3</td><td>incomplete</td></tr>
<tr><td>6.7</td><td>4</td><td>incomplete</td></tr>
</table>

GraphicsMagick
--------------
The (GraphicsMagick Wand API)[http://www.graphicsmagick.org/wand/wand.html] was
forked from ImageMagick in August 2003. It lacks features that are available in
newer versions and therefore, it is currently not support.
As GraphicsMagick focuses on a stable API, it might be interesting to support
it. You are free to add support.

Authors
=======
- Ian Stevens, http://crazedmonkey.com/
- Victor Ng, http://www.monkeybeanonline.com/
- Benjamin Schweizer, http://benjamin-schweizer.de/contact

Todo
====
- complete support for higher API levels (see API Versions above)
- we should add exhaustive unit tests

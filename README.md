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

Authors
-------
- Ian Stevens, http://crazedmonkey.com/
- Victor Ng, http://www.monkeybeanonline.com/
- Benjamin Schweizer, http://benjamin-schweizer.de/contact

Todo
----
- implement new features from MagickWand 6.7
- figure out how to support deprecated features (see magick/deprecate.c)
- we should add exhaustive unit tests

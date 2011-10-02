magickfoo
=========
A more pythonic API for ImageMagick.

About
-----
This folder holds Ian Stevens' original pythonmagickwand[1] API. It is designed
to be more pythonic than the pure MagickWand API, but it implements only a
subset of available features.

[1]: https://www.assembla.com/wiki/show/pythonmagickwand

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
=======
- Ian Stevens, http://crazedmonkey.com/
- Victor Ng, http://www.monkeybeanonline.com/ 
- Benjamin Schweizer, http://benjamin-schweizer.de/contact

Todo
====
- encapsulation of more MagickWand API calls

python-magickwand
=================
Python bindings for the ImageMagick [MagickWand API][1].

About
-----
The [MagickWand API][1] is the recommended interface between the C programming
language and the ImageMagick image processing libraries. This package provides
bindings for the Python language.

[1]: http://www.imagemagick.org/api/magick-wand.php

Examples
========
flip
----
```python
magick_wand = NewMagickWand()
MagickReadImage(magick_wand, 'rose.jpg')
if not MagickFlipImage(magick_wand):
    raise WandException(magick_wand)
MagickWriteImage(magick_wand, "result.jpg")
```

annotate
--------
```python
magick_wand = NewMagickWand()
MagickReadImage(magick_wand, 'rose.jpg')
drawing_wand=NewDrawingWand()
DrawSetFont(drawing_wand, "/usr/share/fonts/bitstream-vera/Vera.ttf")
DrawSetFontSize(drawing_wand, 20)
DrawSetGravity(drawing_wand, CenterGravity)
pixel_wand = NewPixelWand()
PixelSetColor(pixel_wand, "white")
DrawSetFillColor(drawing_wand, pixel_wand)
if not MagickAnnotateImage(magick_wand, drawing_wand, 0, 0, 0, "Rose") != 0:
    raise WandException(magick_wand)
MagickWriteImage(magick_wand, "result.jpg")
```

More samples are available in [the samples directory][2].

[2]: samples/

Compatibility
=============
API Versions
------------
The MagickWand API is available in various versions:

<table>
<tr><td><b>ImageMagick</b></td><td><b>MagickWand</b></td><td><b>Status</b></td></tr>
<tr><td>6.4</td><td>1</td><td>not generated</td></tr>
<tr><td>6.5</td><td>2</td><td>not generated</td></tr>
<tr><td>6.6</td><td>3</td><td>supported</td></tr>
<tr><td>6.7</td><td>4</td><td>supported</td></tr>
</table>

GraphicsMagick
--------------
The [GraphicsMagick Wand API][3] was forked from ImageMagick in August 2003.
It lacks features that are available in newer versions and therefore, it is
currently not supported here.
Though, as GraphicsMagick focuses on a stable API, it would be nice to have
support for it here. Your contrubition is highly welcome.

[3]: http://www.graphicsmagick.org/wand/wand.html

Alternatives
============
PythonMagic
-----------
[PythonMagick][4] provides ImageMagick bindings based on [Boost][5].

PythonMagickWand by Achim Donna
-------------------------------
[PythonMagickWand][6] provides MagickWand bindings based on CDDL; outdated.

PythonMagickWand by Ian Stevens
-------------------------------
[PythonMagickWand][7] is an implementation of the MagickWand API with focus on
a pythonic interface. It provides an object-oriented API on top of the
MagickWand API.

python-magickwand by Benjamin Schweizer
---------------------------------------
[This was][8] an updated version if Ian Stevens' bindings; it finally ended up here.

[4]: http://www.imagemagick.org/download/python/
[5]: http://www.boost.org/
[6]: http://public.procoders.net/PythonMagickWand/docs/html/index.html
[7]: https://www.assembla.com/wiki/show/pythonmagickwand
[8]: http://benjamin-schweizer.de/python-magickwand-or-how-to-work-with-icons.html

Authors
=======
- Benjamin Schweizer, http://benjamin-schweizer.de/contact
- Ian Stevens, http://crazedmonkey.com/
- Victor Ng, http://www.monkeybeanonline.com/ 

Todo
====
- generate bindings for magickwand-1 and magickwand-2
- re-enable win32 support
- possibly, re-enable Ian's pythonic api

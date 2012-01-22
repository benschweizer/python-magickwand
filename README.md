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

[2]: https://github.com/gopher/python-magickwand/tree/master/samples

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
<tr><td>6.7.0</td><td>4</td><td>supported</td></tr>
<tr><td>6.7.2</td><td>5</td><td>supported</td></tr>
</table>

GraphicsMagick
--------------
The [GraphicsMagick Wand API][3] was forked from ImageMagick in August 2003.
It lacks features that are available in newer versions and therefore, it is
currently not supported here.
Though, as GraphicsMagick focuses on a stable API, it would be nice to have
support for it. Your contribution is highly welcome.

[3]: http://www.graphicsmagick.org/wand/wand.html

Alternatives
============
There are various other bindings and abstractions for ImageMagick, here is an onverview:

<pre>
PythonMagick ------- 0.3 -- 0.4 -- 0.5 ---------------- 0.7 --------- 0.8 --------- 0.9.7
                               \
PythonMagickWand/Achim Domma     ---------------------- 0.2 --------- r107

PythonMagickWand/Ian Stevens                                   * ---- r42 -- r53
                                                                        \
python-magickwand/Benjamin Schweizer                                  2009 -------- 2011 - 2012
                                                                            \
python-magickwand/Oliver Berger                                              0.2

Wand                                                                                0.1 -- 0.1.9

                     2002   2003   2004   2005   2006   2007   2008   2009   2010   2011   2012
</pre>

PythonMagick
------------
[PythonMagick][4] is the oldest wrapper for the ImageMagick API. It is a
C++ extension based on the [Boost Library][5] and thus, requires compilation on
OS-level.

[4]: http://www.imagemagick.org/download/python/
[5]: http://www.boost.org/

PythonMagickWand/Achim Domma
----------------------------
Achim Domma stated on PythonMagick that is is too hard to maintain and started
a CDLL-based re-implementation of the MagickWand API. [This version][6] includes
a custom API generator based on [gccxml][7]. Though, it was abandoned in 2008.

[6]: http://public.procoders.net/PythonMagickWand/docs/html/index.html
[7]: http://www.gccxml.org/HTML/Index.html

PythonMagickWand/Ian Stevens
----------------------------
Ian Stevens and Victor Ng started [PythonMagickWand][8]. PythonMagickWand aims
to provide an object-oriented API that is structured to be more pythonic.
Their implementation uses [h2xml and xml2py][9] for MagickWand API generation.
It introduced the Image, Color and MagickWand classes that later influened the
MagickFoo and Wand APIs.

There are two forks, one by Benjamin Schweizer named [python-magickwand][10] and
a fork thereof by Oliver Berger named [python-magickwand-0.2][11]. The first is
a direct predecessor of this source tree, the latter was abandoned in 2010.

[8]: https://www.assembla.com/wiki/show/pythonmagickwand
[9]: http://svn.python.org/projects/ctypes/trunk/ctypeslib/
[10]: http://hg.sickos.org/python-magickwand/
[11]: http://pypi.python.org/pypi/magickwand/

MagickFoo
---------
[MagickFoo][12] is an updated version of Ian Steven's PythonMagickWand API. It is
included in [python-magickwand][13].

[12]: https://github.com/gopher/python-magickwand/magickfoo
[13]: https://github.com/gopher/python-magickwand

Wand/Hong Minhee
----------------
[Wand][14] is a new CDLL-based abstraction by Hong Minhee. It was inspired by
Ian Steven's PythonMagickWand API. As of 2012, the project is in active develop
ment with regular github commits.

[14]: http://styleshare.github.com/wand/

Authors
=======
- Benjamin Schweizer, http://benjamin-schweizer.de/contact
- Ian Stevens, http://crazedmonkey.com/
- Victor Ng, http://www.monkeybeanonline.com/ 

Todo
====
- generate bindings for magickwand-1 and magickwand-2
- re-enable win32 support

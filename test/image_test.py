import ctypes
from StringIO import StringIO
from pythonmagickwand.wand import PIXELS_PER_INCH, PIXELS_PER_CENTIMETER, CMYK_COLORSPACE, BZIP_COMPRESSION
from pythonmagickwand.image import Image
from pythonmagickwand import api, color

GIF = '''\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\xf0\x00\x00\xf0\xe6\x8c\x00\x00\x00\x21\xf9\x04\x00\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b\x00'''
EPS = '''%!PS-Adobe-3.0 EPSF-3.0
%%Creator: Ian Stevens
%%Origin: 0 0
%%BoundingBox: 100 100 200 200
newpath
100 100 moveto
0 100 rlineto
100 0 rlineto
0 -100 rlineto
-100 0 rlineto
closepath
gsave
0 0 0.4 setrgbcolor
fill
'''

def setup():
    i = Image()
    api.MagickNewImage(i._wand, 100, 100, api.NewPixelWand())
    return i

def test_set_format():
    w = setup()
    w.format = 'PNG'
    assert 'PNG' == api.MagickGetImageFormat(w._wand)
    w.format = None
    assert '' == api.MagickGetImageFormat(w._wand)
    try:
        w.format = 'invalid image format'
    except:
        pass
    else:
        assert False

def test_get_format():
    w = Image()
    assert None == w.format
    api.MagickNewImage(w._wand, 100, 100, api.NewPixelWand())
    assert None == w.format
    api.MagickSetImageFormat(w._wand, 'PNG')
    assert 'PNG' == w.format

def test_set_units():
    w = setup()
    w.units = None
    assert api.UndefinedResolution == api.MagickGetImageUnits(w._wand)
    w.units = PIXELS_PER_INCH
    assert PIXELS_PER_INCH == api.MagickGetImageUnits(w._wand)
    try:
        w.units = 12345
    except ValueError:
        pass
    else:
        assert False

def test_get_units():
    w = Image()
    assert None == w.units
    api.MagickNewImage(w._wand, 100, 100, api.NewPixelWand())
    assert None == w.units
    api.MagickSetImageUnits(w._wand, api.PixelsPerInchResolution)
    assert PIXELS_PER_INCH == w.units

def test_set_resolution():
    w = setup()
    w.resolution = (300, 300)
    x = y = ctypes.c_double()
    api.MagickGetImageResolution(w._wand, x, y)
    assert (300, 300) == (x.value, y.value)

def test_get_resolution():
    w = setup()
    assert (72, 72) == w.resolution
    api.MagickSetImageResolution(w._wand, 300, 300)
    assert (300, 300) == w.resolution

def test_get_size():
    w = setup()
    assert (100, 100) == w.size

def test_set_size():
    w = setup()
    w.size = (200, 200)
    width = api.MagickGetImageWidth(w._wand)
    height = api.MagickGetImageHeight(w._wand)
    assert (200, 200) == (width, height)

def test_set_colorspace():
    w = setup()
    w.colorspace = CMYK_COLORSPACE
    assert CMYK_COLORSPACE == api.MagickGetImageColorspace(w._wand)

def test_get_colorspace():
    w = Image()
    assert None == w.colorspace
    w = setup()
    api.MagickSetImageColorspace(w._wand, CMYK_COLORSPACE)
    assert CMYK_COLORSPACE == w.colorspace

def test_set_background_color():
    w = setup()
    c = color.PINK
    w.background_color = c
    c2 = api.NewPixelWand()
    api.MagickGetImageBackgroundColor(w._wand, c2)
    assert api.IsPixelWandSimilar(c2, c._wand, 0)

def test_get_background_color():
    w = setup()
    pw = api.NewPixelWand()
    api.PixelSetColor(pw, 'purple')
    api.MagickSetImageBackgroundColor(w._wand, pw)
    assert api.IsPixelWandSimilar(pw, w.background_color._wand, 0)

def test_set_border_color():
    w = setup()
    c = color.PINK
    w.border_color = c
    c2 = api.NewPixelWand()
    api.MagickGetImageBorderColor(w._wand, c2)
    assert api.IsPixelWandSimilar(c2, c._wand, 0)

def test_get_border_color():
    w = setup()
    pw = api.NewPixelWand()
    api.PixelSetColor(pw, 'purple')
    api.MagickSetImageBorderColor(w._wand, pw)
    assert api.IsPixelWandSimilar(pw, w.border_color._wand, 0)

def test_set_compression():
    w = setup()
    w.compression = BZIP_COMPRESSION
    assert BZIP_COMPRESSION == api.MagickGetImageCompression(w._wand)

def test_get_compression():
    w = setup()
    api.MagickSetImageCompression(w._wand, BZIP_COMPRESSION)
    assert BZIP_COMPRESSION == w.compression

def test_set_compression_quality():
    w = setup()
    w.compression_quality = 55
    assert 55 == api.MagickGetImageCompressionQuality(w._wand)
    w.compression_quality = 55.5
    assert 56 == api.MagickGetImageCompressionQuality(w._wand)

def test_get_compression_quality():
    w = setup()
    api.MagickSetImageCompressionQuality(w._wand, 55)
    assert 55 == w.compression_quality

def test_constructor_with_file():
    w = Image(StringIO(GIF))
    assert 'GIF' == w.format
    assert (1,1) == w.size
    size = api.size_t()
    b = api.MagickGetImageBlob(w._wand, size)
    assert GIF == ''.join([chr(b[i]) for i in range(0, size.value + 1)])

def test_constructor_with_eps_file():
    w = Image(StringIO(EPS))
    assert 'EPS' == w.format
    size = api.size_t()
    b = api.MagickGetImageBlob(w._wand, size)
    assert EPS == ''.join([chr(b[i]) for i in range(0, size.value + 1)])

def test_scale():
    w = setup()
    w.scale((200, 200))
    assert (200, 200) == w.size

def test_resize():
    w = setup()
    w.resize((200, 200))
    assert (200, 200) == w.size
    w.resize((300, 300), filter=None)
    assert (300, 300) == w.size

def test_resample():
    w = setup()
    res = w.resolution
    size = w.size
    w.resample((3*res[0], 2*res[1]))
    assert (3*size[0], 2*size[1]) == w.size

def test_chop():
    w = setup()
    w.chop((10, 10), (50, 50))
    assert (90, 90) == w.size

def test_splice():
    w = setup()
    w.splice((10,10), (50,50))
    assert (110, 110) == w.size

def test_magnify():
    w = setup()
    w.magnify()
    assert (200, 200) == w.size

def test_minify():
    w = setup()
    w.minify()
    assert (50, 50) == w.size


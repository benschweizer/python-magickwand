import ctypes
from pythonmagickwand import api
from pythonmagickwand.color import Color

def test_init_with_color():
    c = Color('#0000ff')
    assert 0 == api.PixelGetRed(c._wand)
    assert 0 == api.PixelGetGreen(c._wand)
    assert 1 == api.PixelGetBlue(c._wand)

def test_images_equal():
    assert Color('blue') == Color('#0000ff')
    assert Color('blue') != Color('#0001ff')
    assert Color('blue') == Color('#0000ffff')
    assert Color('blue') != Color('#0000ff01')

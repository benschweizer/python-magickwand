import ctypes
from StringIO import StringIO
from pythonmagickwand.wand import MagickWand
from pythonmagickwand import api

def test_set_size():
    w = MagickWand()
    w.size = (100, 100)
    x = y = ctypes.c_ulong()
    api.MagickGetSize(w._wand, x, y)
    assert (100, 100) == (x.value, y.value)

def test_get_size():
    w = MagickWand()
    assert (0, 0) == w.size
    api.MagickSetSize(w._wand, 100, 100)
    assert (100, 100) == w.size

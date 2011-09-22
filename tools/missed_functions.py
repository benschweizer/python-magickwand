#!/usr/bin/env python
#
# this is a helper script to check the local magickwand library for new,
# yet unwrapped functions that should be added to these bindings.

import sys; sys.path.insert(0, '..')
import subprocess
from ctypes import *
from ctypes.util import find_library

from magickwand import api

# fixme: should use realpath, need to deal with ld and scan libpath
#wand_lib = find_library('MagickWand')
wand_lib = '/usr/lib64/libMagickWand.so.3'
if not wand_lib:
    raise ImportError('Cannot find ImageMagick MagickWand library.')
print "found library: %s" % wand_lib

_lib = CDLL(wand_lib)

p = subprocess.Popen(['readelf', '-Ws', wand_lib], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
if stderr:
    raise Exception(stderr)

for line in stdout.split("\n"):
    try:
        num, value, size, stype, bind, vis, ndx, name = line.split()
        size=int(size)
    except ValueError:
        continue
    if size and not hasattr(api, name):
        print "%s not yet wrapped" % name 

# eof.

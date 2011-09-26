# ImageMagick MagickWand API Wrapper
#

from ctypes.util import find_library

wand_lib = find_library('MagickWand')
if not wand_lib:
    raise ImportError('MagickWand library cannot be found.')

if wand_lib in ['libMagickWand.so.1']:
    raise ImportError('api bindings for version 1 are not available, please file a bug')
    wand_version = 1
    from magickwand1 import *
elif wand_lib in ['libMagickWand.so.2']:
    raise ImportError('api bindings for version 2 are not available, please file a bug')
    wand_version = 2
    from magickwand2 import *
elif wand_lib in ['libMagickWand.so.3']:
    wand_version = 3
    from magickwand3 import *
elif wand_lib in ['libMagickWand.so.4']:
    wand_version = 4
    from magickwand4 import *
else:
    raise ImportError('API level is not supported or mapping is incomplete: ' + wand_lib)

# eof.

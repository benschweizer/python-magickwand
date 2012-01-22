# ImageMagick MagickWand API Wrapper
#

from ctypes.util import find_library

wand_lib = find_library('MagickWand')
if not wand_lib:
    raise ImportError('MagickWand library cannot be found.')

if wand_lib in ['libMagickWand.so.1']:
    raise ImportError('API level 1 was not implemented, please file a bug')
    wand_version = 1
    from magickwand1 import *
elif wand_lib in ['libMagickWand.so.2']:
    raise ImportError('API level 2 was not implemented, please file a bug')
    wand_version = 2
    from magickwand2 import *
elif wand_lib in ['libMagickWand.so.3']:
    wand_version = 3
    from magickwand3 import *
elif wand_lib in ['libMagickWand.so.4']:
    wand_version = 4
    from magickwand4 import *
elif wand_lib in ['libMagickWand.so.5']:
    wand_version = 5
    from magickwand5 import *
else:
    raise ImportError('API level could be mapped, found ' + wand_lib)

class WandException(Exception):
    def __init__(self, wand):
        self.severity = ExceptionType()
        self.description = MagickGetException(wand, self.severity)

    def __str__(self):
        return repr(self.description)

# eof.

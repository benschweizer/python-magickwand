from magickwand import *

magick_wand = NewMagickWand()
MagickReadImage(magick_wand, 'rose.jpg')
if not MagickFlipImage(magick_wand):
    severity = ExceptionType()
    description = MagickGetException(magick_wand, severity)
    raise Exception(description)
MagickWriteImage(magick_wand, "result.jpg")

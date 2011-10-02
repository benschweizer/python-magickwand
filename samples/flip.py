from magickwand import *

magick_wand = NewMagickWand()
MagickReadImage(magick_wand, 'rose.jpg')
if not MagickFlipImage(magick_wand):
    raise WandException(magick_wand)
MagickWriteImage(magick_wand, "result.jpg")

from magickwand import *

def convert(wand, width, height, depth):
    """extrace or convert image to given dimensions"""
    MagickResetIterator(wand)
    # i) find exact match
    has_image= True
    while has_image:
        _width = MagickGetImageWidth(wand)
        _height = MagickGetImageHeight(wand)
        _depth = MagickGetImageChannelDepth(wand, AlphaChannel)
        if _width == width and _height == height and _depth == depth:
            return wand
        has_image = MagickNextImage(wand)

    # ii) find any match
    MagickResetIterator(wand)
    has_image= True
    while has_image:
        _width = MagickGetImageWidth(wand)
        _height = MagickGetImageHeight(wand)
        if _width == width and _height == height:
            return wand
        has_image = MagickNextImage(wand)

    # iii) fall back to scaling
    if not MagickScaleImage(wand, width, height):
        severity = ExceptionType()
        description = MagickGetException(magick_wand, severity)
        raise Exception(description)
    return wand

magick_wand = NewMagickWand()
MagickReadImage(magick_wand, 'favicon.ico')
magick_wand = convert(magick_wand, 16, 16, 8)
MagickWriteImage(magick_wand, "favicon.png")

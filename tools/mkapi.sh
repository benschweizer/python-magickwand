#/bin/sh
#
h2xml -I /usr/include/ImageMagick/ /usr/include/ImageMagick/wand/MagickWand.h /usr/include/ImageMagick/wand/*h -o api.xml -q -c
xml2py api.xml -l /usr/lib/libMagickWand.so.3 -k f > api.py
# eof.

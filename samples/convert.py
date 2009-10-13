#!/usr/bin/env python

from magickwand.image import Image

def convert(source_fh, source_type, dest_type, dest_size):
    """somewhat like convert(1)"""
    i = Image(source_fh, source_type)

    if not i.select(dest_size):
        print "bad size"
        i.alpha(True)
        i.scale(dest_size)

    i.alpha(True)
    result = i.dump(dest_type)

    return result

if __name__=='__main__':
    source_fh = open('favicon.ico', 'r')
    dest_buf = convert(source_fh, 'ico', 'png', (16,16))
    open('favicon.png', 'wb').write(dest_buf)

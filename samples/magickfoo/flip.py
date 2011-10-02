from magickfoo import Image

image = Image('foo.jpg')
image.format = 'PNG'
image.flip()
image.save('flip.png')

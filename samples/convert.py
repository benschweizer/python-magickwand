from magickwand.image import Image

image = Image('favicon.ico')
image.convert(size=(16,16),depth=8)
image.save('favicon.png')

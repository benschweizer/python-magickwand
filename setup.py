from setuptools import setup, find_packages

setup(
        # name = "PythonMagickWand",
        # author = "Ian Stevens",
        # author_email = "icstevens@hotmail.com",
        # url = "http://www.assembla.com/wiki/show/pythonmagickwand",
        # description = "Python bindings for ImageMagick's MagickWand",
        # version = "0.1",
        name = "python-magickwand",
        author = "Benjamin Schweizer",
        author_email = "web09@benjamin-schweizer.de",
        url = "http://hg.sickos.org/python-magickwand",
        description = "Python bindings for ImageMagick's MagickWand",
        version = "0.2sickos",
        packages = find_packages(exclude='test'),
     )

from setuptools import setup, find_packages

setup(
        name = "python-magickwand",
        author = "Benjamin Schweizer",
        author_email = "code@benjamin-schweizer.de",
        url = "https://github.com/gopher/python-magickwand",
        description = "Python bindings for the ImageMagick MagickWand C-API",
        version = "git",
        packages = find_packages(exclude='tools'),
     )

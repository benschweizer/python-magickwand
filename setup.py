from setuptools import setup, find_packages

setup(
        name = "PythonMagickWand",
        author = "Ian Stevens",
        author_email = "icstevens@hotmail.com",
        url = "http://www.assembla.com/wiki/show/pythonmagickwand",
        description = "Python bindings for ImageMagick's MagickWand",
        version = "0.1",
        packages = find_packages(exclude='test'),
     )

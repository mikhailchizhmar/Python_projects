from setuptools import setup
from Cython.Build import cythonize

"""python setup.py install"""

setup(
    name='matrix',
    ext_modules=cythonize("multiply.pyx")
)

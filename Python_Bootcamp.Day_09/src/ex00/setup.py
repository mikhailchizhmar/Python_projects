from setuptools import setup, Extension

"""python setup.py install"""

calculator_module = Extension('calculator', sources=['calculator.c'])
setup(
    name='calculator',
    version='1.0',
    description='A simple calculator module',
    ext_modules=[calculator_module]
)

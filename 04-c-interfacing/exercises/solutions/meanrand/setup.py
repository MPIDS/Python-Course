"""
To compile run python setup.py build_ext -i.
"""

from distutils.core import setup, Extension

setup(
    ext_modules = [
        Extension("_meanrand", sources=["meanrand.c", "meanrand.i"])
    ]
)

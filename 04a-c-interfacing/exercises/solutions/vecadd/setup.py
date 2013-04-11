"""
To compile run python setup.py build_ext -i.
"""

from distutils.core import setup, Extension

setup(
    ext_modules = [
        Extension("_vecadd", sources=["vecadd.c", "vecadd.i"])
    ]
)

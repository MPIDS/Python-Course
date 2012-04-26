"""
To compile run python setup.py build_ext -i.
"""

from distutils.core import setup, Extension

setup(
    ext_modules = [
        Extension("_geomean", sources=["geomean.c", "geomean.i"])
    ]
)

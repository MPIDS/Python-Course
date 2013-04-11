from distutils.core import setup, Extension
setup(
    ext_modules = [
        Extension("_cdtw", \
                  sources=["cdtw.c", "cdtw.i"])
    ]
)

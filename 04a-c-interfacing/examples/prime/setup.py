from distutils.core import setup, Extension
setup(
    ext_modules = [
        Extension("_primetest", \
                  sources=["primetest.c", "primetest.i"])
    ]
)

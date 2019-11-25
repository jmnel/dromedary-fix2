from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

#sourcefiles = ['solver/solver.py']

extensions = [
        Extension('solver', ['solver/solver.py']),
        Extension('GUI', ['solver/GUI.py'])
        ]

setup(
    ext_modules=cythonize(extensions)
)

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='test solver app',
    ext_modules = cythonize('solver/*.py', compiler_directives={'language_level': '3'})
    )

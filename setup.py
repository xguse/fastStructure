#
# from distutils.core import setup
# from distutils.extension import Extension
# from Cython.Distutils import build_ext
# import numpy
# import sys
#
# # setup bed parser
# ext_modules = [Extension("parse_bed", ["fastStructure/parse_bed.pyx"])]
#
# setup(
#     name='parse_bed',
#     cmdclass={'build_ext': build_ext},
#     include_dirs=[numpy.get_include(), '.'],
#     ext_modules=ext_modules
# )
#
# # setup structure format parser
# ext_modules = [Extension("parse_str", ["fastStructure/parse_str.pyx"])]
#
# setup(
#     name='parse_str',
#     cmdclass={'build_ext': build_ext},
#     include_dirs=[numpy.get_include(), '.'],
#     ext_modules=ext_modules
# )
#
# # setup fastStructure
# ext_modules = [Extension("fastStructure", ["fastStructure/fastStructure.pyx"])]
#
# setup(
#     name='fastStructure',
#     cmdclass={'build_ext': build_ext},
#     include_dirs=[numpy.get_include(), '.', 'fastStructure/vars/'],
#     ext_modules=ext_modules
# )


from setuptools import setup, find_packages
from distutils.extension import Extension
import numpy

# setuptools DWIM monkey-patch madness
# http://mail.python.org/pipermail/distutils-sig/2007-September/thread.html#8204
import sys

if 'setuptools.extension' in sys.modules:
    m = sys.modules['setuptools.extension']
    m.Extension.__dict__ = m._Extension.__dict__




include_dirs_common = [numpy.get_include(), 'fastStructure']
library_dirs_common = ["/usr/local/lib"]
extra_compile_args_common = ["-I/usr/local/include",
                    "-L/usr/local/lib"]

setup(
    name='fastStructure',
    author='Anil Raj',
    version='1.0',
    author_email='rajanil@stanford.edu',
    license='MIT',

    packages=find_packages(),

    setup_requires=[
        'setuptools-cython',
    ],

    install_requires=[
        "numpy",
        "scipy",
        "cython",
    ],

    ext_modules=[
        Extension(name="parse_bed",
        sources=["fastStructure/parse_bed.pyx"],
        include_dirs=include_dirs_common,
        library_dirs=library_dirs_common,
        extra_compile_args=extra_compile_args_common),

        Extension(name="parse_str",
        sources=["fastStructure/parse_str.pyx"],
        include_dirs=include_dirs_common,
        library_dirs=library_dirs_common,
        extra_compile_args=extra_compile_args_common),

        Extension(name="fastStructure",
        sources=["fastStructure/fastStructure.pyx"],
        include_dirs=include_dirs_common + ['fastStructure/vars/'],
        library_dirs=library_dirs_common,
        extra_compile_args=extra_compile_args_common),

    ],

    # set up command-line executables the python way instead of calling full paths like barbarians
    entry_points={
        'console_scripts': [
            'structure = fastStructure.structure:main',
            'chooseK = fastStructure.chooseK:main',
            'distruct = fastStructure.distruct:main',
        ]
    }
)

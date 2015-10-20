
from setuptools import setup, find_packages
from distutils.extension import Extension
import numpy

include_dirs_common = [numpy.get_include(), 'fastStructure', '.']
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
            extra_compile_args=extra_compile_args_common
        ),

        Extension(name="parse_str",
            sources=["fastStructure/parse_str.pyx"],
            include_dirs=include_dirs_common,
            library_dirs=library_dirs_common,
            extra_compile_args=extra_compile_args_common
        ),

        Extension(name="fastStructure",
            sources=["fastStructure/fastStructure.pyx"],
            include_dirs=include_dirs_common + ['fastStructure/vars/'],
            library_dirs=library_dirs_common,
            extra_compile_args=extra_compile_args_common
        ),

        # ##  from the vars package
        Extension(name="fastStructure.vars.utils",
            sources=["fastStructure/vars/utils.pyx"],
            include_dirs=include_dirs_common,
            library_dirs=library_dirs_common,
            extra_compile_args=extra_compile_args_common
        ),

        Extension(name="fastStructure.vars.admixprop",
            sources=["fastStructure/vars/admixprop.pyx", "fastStructure/vars/C_admixprop.c"],
            include_dirs=include_dirs_common,
            library_dirs=library_dirs_common,
            extra_compile_args=extra_compile_args_common
        ),

        Extension(name="fastStructure.vars.allelefreq",
            sources=["fastStructure/vars/allelefreq.pyx", "fastStructure/vars/C_allelefreq.c"],
            include_dirs=include_dirs_common,
            library_dirs=library_dirs_common,
            libraries=["gsl","gslcblas"],
            extra_compile_args=extra_compile_args_common + ["-O3"]
        ),

        Extension(name="fastStructure.vars.marglikehood",
            sources=["fastStructure/vars/marglikehood.pyx", "fastStructure/vars/C_marglikehood.c"],
            include_dirs=include_dirs_common,
            library_dirs=library_dirs_common,
            extra_compile_args=extra_compile_args_common
        )

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

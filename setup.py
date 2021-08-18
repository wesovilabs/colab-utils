from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open(os.path.join(_here, 'colab-utils', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='colab-utils',
    version=version['__version__'],
    description=('Set of utilities for Google colabs'),
    long_description=long_description,
    author='Iván Corrales Solera',
    author_email='ivan.corrales.solera@gmail.com',
    url='https://github.com/wesovilabs/colab-utils',
    packages=['colab-utils'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.9'
    ],
    
)
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='latex',
    version='0.6.3',
    description='Wrappers for calling LaTeX/building LaTeX documents.',
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='http://github.com/mbr/latex',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['tempdir', 'data', 'future', 'shutilwhich'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)

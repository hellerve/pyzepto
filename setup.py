#!/usr/bin/env python
from distutils.core import setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name = 'pyzepto',
    description = 'Allows you to interface Python and zepto crudely',
    author = "Veit Heller",
    author_email = "veit@veitheller.de",
    version = "0.0.3",
    long_description = long_description,
    url = "https://github.com/hellerve/pyzepto",
    packages = ['pyzepto',],
    license = "MIT",
    platforms = ['Linux', 'OS X', 'Windows']
)



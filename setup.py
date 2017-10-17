#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from gaccho_twitter import __author__, __version__, __license__

setup(
        name             = 'gaccho_twitter',
        version          = __version__,
        description      = 'Gaccho Twitter Plugin',
        license          = __license__,
        author           = __author__,
        author_email     = 'test@example.com',
        url              = 'https://github.com/nobiki/gaccho_twitter.git',
        keywords         = 'gaccho twitter',
        packages         = find_packages(),
        install_requires = [],
        )


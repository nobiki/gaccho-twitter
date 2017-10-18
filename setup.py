#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from gaccho_twitter import __author__, __version__, __license__

setup(
        name             = 'gaccho_twitter',
        version          = '0.0.1',
        description      = 'Gaccho Twitter Plugin',
        license          = 'MIT',
        author           = 'nobiki',
        author_email     = 'test@example.com',
        url              = 'https://github.com/nobiki/gaccho_twitter.git',
        keywords         = 'gaccho twitter',
        packages         = find_packages(),
        install_requires = [],
        )


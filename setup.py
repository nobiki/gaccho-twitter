#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
        name             = 'gaccho_twitter',
        version          = '0.1.3',
        description      = 'Gaccho Twitter Plugin',
        license          = 'MIT',
        author           = 'nobiki',
        author_email     = 'test@example.com',
        url              = 'https://github.com/nobiki/gaccho_twitter.git',
        keywords         = 'gaccho twitter',
        packages         = find_packages(),
        install_requires = [
            "twitter==1.18.0",
            ],
        )


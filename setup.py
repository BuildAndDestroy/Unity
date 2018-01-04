#!/usr/bin/env python
"""
	To install, run:
	sudo pip install .
	If upgrading, run:
	sudo pip install --upgrade .
"""

from setuptools import setup

__version__ = '1.0'
__author__ = 'Mitch O\'Donnell'
packages = ['network_utility']
commands = ['server_client = network_utility.server_client:main']


setup(
    name                    = 'Network Utilities',
    version                 = __version__,
    description             = 'Network Utilities to help with communicating between devices.',
    author                  =__author__,
    author_email            = 'devreap1@gmail.com',
    packages                = packages,
    url                     = '',
    license                 = open('LICENSE').read(),
    install_requirements    = [''],
    entry_points            = {'console scripts': commands},
    prefix                  = '/opt/Network_Utilities',
    long_description        = open('README.md').read()
)
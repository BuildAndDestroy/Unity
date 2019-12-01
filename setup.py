#!/usr/bin/env python
"""
	To install, run:
	sudo pip install .
	If upgrading, run:
	sudo pip install --upgrade .
"""

from setuptools import setup

__version__ = '5.0-send-mail'
__author__ = 'Mitch O\'Donnell'
packages = ['mailer', 'network_utility', 'web_scraper', 'scripts']
commands = ['unity_client = scripts.unity_client:main',
            'unity_send_mail = scripts.unity_send_mail:main',
            'unity_server = scripts.unity_server:main',
            'unity_scraper = scripts.unity_scraper:main']


setup(
    name                    = 'Unity',
    version                 = __version__,
    description             = 'Network Utilities to help with communicating between devices.',
    author                  =__author__,
    author_email            = 'devreap1@gmail.com',
    packages                = packages,
    url                     = '',
    license                 = open('LICENSE').read(),
    install_requires        = ['argparse', 'requests', 'prettytable'],
    entry_points            = {'console_scripts': commands},
    prefix                  = '/opt/Unity',
    long_description        = open('README.md').read()
)

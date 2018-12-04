#!/usr/bin/env python
"""Linux crawler to pull file system information to exploit.

Crawl the entire linux File system for detailed information.
This will help gather details faster and hopefully help with
escalating privileges or obtain a useful shell.
"""

import argparse
import os

import prettytable

class Debian(object):
    """docstring for ClassName"""
    def __init__(self, user):
        self.home = return_home_content
        self.root = return_root_directory
        self.hosts = '/etc/hosts'
        self.hostname = '/etc/hostname'
        self.hosts_allow = '/etc/hosts.allow'
        self.hosts_deny = '/etc/hosts.deny'
        self.user = user
        self.passwd = return_passwd_content

    @property
    def return_home_content():
        """Return the home user content."""
        home_directory = ['/home/']

    @property
    def return_root_directory():
        """Return root directory content."""
        root_directory = ['/root/']

    @property
    def return_passwd_content():
        """Returns the passwd content."""
        passwd_file = ['/etc/passwd']
        passwd_file_contents = []
        with open('/etc/passwd', 'r') as opened_file:
            open_file_content = opened_file.read()
            passwd_file_contents.append(open_file_content)
        header_content = [passwd_file, passwd_file_contents]
        return header_content

class Rhel(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        self.arg = arg
        


def display_directories(parse_directory):
    """Parse a directory to view contents."""
    get_directory_content = os.listdir(parse_directory)
    return get_directory_content

def print_pretty_directories(parse_directories):
    """Parse a directory list to display in a table."""
    pass


def main():
    """Execute to pull all details on the Linux file system."""
    pass

if __name__ == '__main__':
    main()
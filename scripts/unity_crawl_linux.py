#!/usr/bin/env python
"""Linux crawler to pull file system information to exploit.

Crawl the entire linux File system for detailed information.
This will help gather details faster and hopefully help with
escalating privileges or obtain a useful shell.
"""

import os

class Debian(object):
    """docstring for ClassName"""
    def __init__(self, user):
        self.home = '/home/'
        self.user = self.home + user


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
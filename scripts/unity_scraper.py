#!/usr/bin/env python
"""Web scraper for everything online.

The concept here is to use Python as a webscraper for online material.
This will also work on Tor hidden sites.
"""

import argparse

import prettytable
from web_scraper.web_utils import RequestSite


def parse_arguments():
    """Help menu with our tool's arguments"""
    legal_statement = 'Copyright (C) 2017  Mitch O\'Donnell\n    This program comes with ABSOLUTELY NO WARRANTY.\n    This is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url = 'https://github.com/BuildAndDestroy/Unity'
    epilog = '[*] Webscraper for given URLs.\n\r[*] {}\n\r[*] {}'.format(
        url, legal_statement)
    parser = argparse.ArgumentParser(
        epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('urls', nargs='*',
                        help='Apply multiple URLs for scanning.')
    parser.add_argument('-s', '--ssl', action='store_true',
                        help='Verify the SSL of requested website.')
    parser.add_argument('-t', '--tor', action='store_true',
                        help='Route through the Tor network.')
    parser.add_argument('-l', '--landing', action='store_true',
                        help='Print the landing page for url requested.')
    parser.add_argument('-g', '--get_headers', action='store_true',
                        help='Print Headers sent back from the requested URL.')
    parser.add_argument('-c', '--cookies', action='store_true',
                        help='Print Cookies the site has registered for this session.')
    parser.add_argument('-r', '--response', action='store_true',
                        help='Return site status code.')
    parser.add_argument('-p', '--pretty', action='store_true',
                        help='Format into tables and print.')

    args = parser.parse_args()
    return args


def table_format(header_list, data_dictionary):
    """Take site requests and print to table format."""
    table = prettytable.PrettyTable(header_list)
    for key, value in data_dictionary.iteritems():
        table.add_row([key, value])
    print table


def main():
    """Scrape websites for usable data."""
    args = parse_arguments()

    for url in args.urls:
        site_requested = RequestSite(url, args.ssl, args.tor)
        if args.response:
            if args.pretty:
                table_format([site_requested.url, 'Response'],
                             site_requested.return_site_status())
            else:
                print '{}: {}'.format(url, site_requested.return_site_status())
        if args.get_headers:
            if args.pretty:
                table_format([site_requested.url, 'Headers'],
                             site_requested.return_site_headers())
            else:
                print '{}: {}'.format(
                    url, site_requested.return_site_headers())
        if args.cookies:
            if args.pretty:
                table_format([site_requested.url, 'Cookies'],
                             site_requested.return_site_cookies())
            else:
                print '{}: {}'.format(
                    url, site_requested.return_site_cookies())
        if args.landing:
            print '[*] {}'.format(url)
            print site_requested.return_site_text()


if __name__ == '__main__':
    main()

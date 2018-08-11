#!/usr/bin/env python
"""Web scraper for everything online.

The concept here is to use Python as a webscraper for online material.
This will also work on Tor hidden sites.
"""

import argparse

import requests

import prettytable


class RequestSite(object):
    """Website scraper Class."""

    def __init__(self, url, ssl, tor):
        self.url = url
        self.tor = tor
        self.ssl = ssl
        self.my_user_agent = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        self.session = requests.session()
        self.site_response = self.request_site
        self.site_status_code = self.site_response.status_code
        self.site_headers = self.site_response.headers
        self.site_cookies = self.site_response.cookies
        self.site_text = self.site_response.text

    @property
    def request_site(self):
        """Request site with or without tor."""
        if self.tor:
            self.session.proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        site_request = self.session.get(
            self.url, headers=self.my_user_agent, verify=self.ssl)
        return site_request

    def return_site_status(self):
        """Return site status code response."""
        site_status_dictionary = {}
        site_status_dictionary['Site Status'] = self.site_status_code
        return site_status_dictionary

    def return_site_headers(self):
        """Return the headers in key, value format."""
        headers_dictionary = {}
        for key, value in self.site_headers.iteritems():
            headers_dictionary[key] = value
        return headers_dictionary

    def return_site_cookies(self):
        """Return cookies from website response."""
        site_cookies = {}
        for key, value in self.site_cookies.iteritems():
            site_cookies[key] = value
        return site_cookies

    def return_site_text(self):
        """Return the landing page content."""
        return self.site_text


def table_format(header_dictionary, data_dictionary):
    """Take site requests and print to table format."""
    table = prettytable.PrettyTable(header_dictionary)
    for key, value in data_dictionary.iteritems():
        table.add_row([key, value])
    print table


def parse_arguments():
    """Help menu with our tool's arguments"""
    epilog = '[*] Webscraper for a given URL.\n\r'
    parser = argparse.ArgumentParser(
        epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('urls', nargs='*',
                        help='Apply multiple URLs for scanning.')
    parser.add_argument('-s', '--ssl', action='store_true',
                        help='Verify the SSL of requested website.')
    parser.add_argument('-t', '--tor', action='store_true',
                        help='Route through the Tor network.')
    parser.add_argument('-c', '--content', action='store_true',
                        help='Print the landing page content requested.')
    parser.add_argument('-H', '--headers', action='store_true',
                        help='Print Headers sent back from the requested URL.')
    parser.add_argument('-k', '--cookies', action='store_true',
                        help='Print Cookies the site has registered for this session.')
    parser.add_argument('-f', '--format', action='store_true', help='Format into tables and print.')
    parser.add_argument('-r', '--response', action='store_true', help='Return site status code.')

    args = parser.parse_args()
    return args


def main():
    """Scrape websites for usable data."""
    args = parse_arguments()

    print args

    for url in args.urls:
        site_requested = RequestSite(url, args.ssl, args.tor)
        if args.format:
            if args.response:
                table_format([site_requested.url, 'Response'],
                         site_requested.return_site_status())
            if args.headers:
                table_format([site_requested.url, 'Headers'],
                             site_requested.return_site_headers())
            if args.cookies:
                table_format([site_requested.url, 'Cookies'],
                             site_requested.return_site_cookies())
            if args.content:
                print site_requested.return_site_text()


if __name__ == '__main__':
    main()

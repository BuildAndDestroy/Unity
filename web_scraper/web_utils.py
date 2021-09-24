#!/usr/bin/env python3
"""Library for online utils.

Library for web browser based content.
"""

import requests


class RequestSite(object):
    """Website scraper Class."""

    def __init__(self, url, ssl, tor) -> None:
        self.url = url
        self.tor = tor
        self.ssl = ssl
        self.session = requests.session()
        self.site_response = self.request_site
        self.site_status_code = self.site_response.status_code
        self.site_headers = self.site_response.headers
        self.site_cookies = self.site_response.cookies
        self.site_text = self.site_response.text

    @property
    def request_site(self) -> None:
        """Request site with or without tor."""
        my_user_agent = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        if self.tor:
            self.session.proxies = {
                'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        site_request = self.session.get(
            self.url, headers=my_user_agent, verify=self.ssl)
        return site_request

    def return_site_status(self) -> dict:
        """Return site status code response."""
        site_status_dictionary = {}
        site_status_dictionary['Site Status'] = self.site_status_code
        return site_status_dictionary

    def return_site_headers(self) -> dict:
        """Return the headers in key, value format."""
        headers_dictionary = {}
        for key, value in self.site_headers.items():
            headers_dictionary[key] = value
        return headers_dictionary

    def return_site_cookies(self) -> dict:
        """Return cookies from website response."""
        site_cookies = {}
        for key, value in self.site_cookies.items():
            site_cookies[key] = value
        return site_cookies

    def return_site_text(self) -> str:
        """Return the landing page html."""
        return self.site_text

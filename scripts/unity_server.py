#!/usr/bin/env python
"""TCP/UDP client and server.

Copyright (C) 2017  Mitch O'Donnell devreap1@gmail.com
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import argparse

from network_utility.server_client import NetworkTools


def parse_arguments():
    """Obtain tcp/udp client or server specification then parse the host and port details."""
    legal_statement = 'Copyright (C) 2017  Mitch O\'Donnell\n    This program comes with ABSOLUTELY NO WARRANTY.\n    This is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url = 'https://github.com/BuildAndDestroy/Unity'
    epilog = '[*] TCP/UDP Server.\n\r[*] {}\n\r[*] {}'.format(
        url, legal_statement)
    parser = argparse.ArgumentParser(
        description=__doc__, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    subparsers = parser.add_subparsers(help='commands', dest='command')

    tcp_server_subparser = subparsers.add_parser(
        'tcp', help='Create a TCP server.')
    tcp_server_subparser.add_argument(
        'host', help='IPv4 Address of ethernet device for binding.')
    tcp_server_subparser.add_argument(
        'port', help='Port number we are binding, must be integer.')

    udp_server_subparser = subparsers.add_parser(
        'udp', help='Create a UDP server.')
    udp_server_subparser.add_argument(
        'host', help='IPv4 Address of ethernet device for binding.')
    udp_server_subparser.add_argument(
        'port', help='Port number we are binding, must be integer.')

    args = parser.parse_args()
    return args


def main():
    """Parse user arguments for tcp/udp server, then bind to host and port."""
    args = parse_arguments()

    if args.command == 'tcp':
        tcp_server = NetworkTools(args.port, args.host)
        tcp_server.tcp_server()

    if args.command == 'udp':
        udp_server = NetworkTools(args.port, args.host)
        udp_server.udp_server()


if __name__ == '__main__':
    main()

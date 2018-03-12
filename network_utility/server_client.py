#!/usr/bin/env python
"""
    TCP/UDP client and server.

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
import socket


class NetworkTools(object):
    """
        Networking Class for tcp client and/or server.
    """

    def __init__(self, port, host=None):
        self.host = host or None
        self.port = int(port)
        self.s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tcp_server(self):
        """A TCP Server that binds to host and port."""
        self.s_tcp.bind((self.host, self.port))
        print '[*] TCP Server binding to {}, listening on port {}.'.format(
            self.host, self.port)
        self.s_tcp.listen(5)
        data_client, addr = self.s_tcp.accept()
        print 'Connection from {}'.format(addr)
        while True:
            data = data_client.recv(1024)
            if not data:
                break
            print 'From connected User {} on port {}, message: {}'.format(
                addr[0], addr[1], data)
            data = str(data).upper()
            print 'Sending {}'.format(data)
            data_client.send(data)
        data_client.close()

    def tcp_client(self):
        """A TCP client that binds to a host and port."""
        self.s_tcp.connect((self.host, self.port))
        print '[*] Connected to {} on port {}.'.format(self.host, self.port)
        print 'Type \'q\' to quit.'
        message = str(raw_input('-> '))
        while message != 'q':
            self.s_tcp.send(message)
            data = self.s_tcp.recv(1024)
            print 'Received from server: {}'.format(data)
            message = str(raw_input('-> '))
        self.s_tcp.close()

    def udp_server(self):
        """UDP server that binds to user provided host and port."""
        self.s_udp.bind((self.host, self.port))
        print '[*] UDP Server binding to {}, listening on port {}.'.format(
            self.host, self.port)
        while True:
            data, address = self.s_udp.recvfrom(1024)
            if not data:
                break
            data = str(data).upper()
            print '[*] From connected User {} on port {}, message:\n {}'.format(
                address[0], address[1], data)
            if data == 'Q':
                self.s_udp.sendto('Server disconnected.', address)
                self.s_udp.close()
                return
            self.s_udp.sendto('ACK', address)
        self.s_udp.close()

    def udp_client(self):
        """UDP client to connect to a UDP server."""
        address = (self.host, 9099)
        server = (self.host, self.port)
        self.s_udp.bind(address)
        print '[*] Type \'q\' to quit.'
        message = str(raw_input('-> '))
        while message != 'q':
            self.s_udp.sendto(message, server)
            data, address = self.s_udp.recvfrom(1024)
            print '[*] Received from server {}, listening on port {}:\n {}'.format(
                self.host, self.port, data)
            message = str(raw_input('-> '))
        self.s_udp.sendto(message, server)
        data, address = self.s_udp.recvfrom(1024)
        print '[*] Received from server {}, listening on port {}:\n {}'.format(
            self.host, self.port, data)
        self.s_udp.close()


def parse_arguments():
    """Obtain tcp/udp client or server specification then parse the host and port details."""
    legal_statement = 'server_client.py Copyright (C) 2017  Mitch O\'Donnell\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url = 'https://github.com/BuildAndDestroy/Unity'
    epilog = '{}\n\n{}'.format(url, legal_statement)
    parser = argparse.ArgumentParser(
        description=__doc__, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)

    subparsers = parser.add_subparsers(help='commands', dest='command')

    tcp_client_subparser = subparsers.add_parser(
        'tcp_client', help='Create a TCP client.')
    tcp_client_subparser.add_argument(
        'host', help='IPv4 Address of ethernet device for binding.')
    tcp_client_subparser.add_argument(
        'port', help='Port number we are binding, must be integer.')

    tcp_server_subparser = subparsers.add_parser(
        'tcp_server', help='Create a TCP server.')
    tcp_server_subparser.add_argument(
        'host', help='IPv4 Address of ethernet device for binding.')
    tcp_server_subparser.add_argument(
        'port', help='Port number we are binding, must be integer.')

    udp_client_subparser = subparsers.add_parser(
        'udp_client', help='Create a UDP client.')
    udp_client_subparser.add_argument(
        'host', help='IPv4 Address of ethernet device for binding.')
    udp_client_subparser.add_argument(
        'port', help='Port number we are binding, must be integer.')

    udp_server_subparser = subparsers.add_parser(
        'udp_server', help='Create a UDP server.')
    udp_server_subparser.add_argument(
        'host', help='IPv4 Address of ethernet device for binding.')
    udp_server_subparser.add_argument(
        'port', help='Port number we are binding, must be integer.')

    args = parser.parse_args()
    return args


def main():
    """Parse user arguments for tcp/udp client or server, then bind to host and port."""
    args = parse_arguments()

    if args.command == 'tcp_server':
        tcp_server = NetworkTools(args.port, args.host)
        tcp_server.tcp_server()
    if args.command == 'tcp_client':
        tcp_client = NetworkTools(args.port, args.host)
        tcp_client.tcp_client()

    if args.command == 'udp_server':
        udp_server = NetworkTools(args.port, args.host)
        udp_server.udp_server()
    if args.command == 'udp_client':
        udp_client = NetworkTools(args.port, args.host)
        udp_client.udp_client()


if __name__ == '__main__':
    main()

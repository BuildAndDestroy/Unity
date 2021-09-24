#!/usr/bin/env python3
"""TCP/UDP client and server library.

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

import socket


class NetworkTools(object):
    """
        Networking Class for tcp/udp client/server.
    """

    def __init__(self, port, host=None) -> None:
        self.host = host or None
        self.port = int(port)
        self.s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tcp_server(self) -> None:
        """A TCP Server that binds to host and port."""
        self.s_tcp.bind((self.host, self.port))
        print(
            f'[*] TCP Server binding to {self.host}, listening on port {self.port}.')
        self.s_tcp.listen(5)
        data_client, addr = self.s_tcp.accept()
        print(f'Connection from {addr}')
        while True:
            data = data_client.recv(1024)
            if not data:
                break
            print(
                f'From connected User {addr[0]} on port {addr[1]}, message: {data}')
            decode_from_bytes_to_str = data.decode()
            data = decode_from_bytes_to_str
            #print(data) # Python3 requires bytes to be sent - hack it for now but fix later to something cleaner
            data = str(data).upper()
            encode_to_bytes = str.encode(data)
            data = encode_to_bytes
            #print(f'Sending {data}')
            data_client.send(data)
        data_client.close()

    def tcp_client(self) -> None:
        """A TCP client that binds to a host and port."""
        self.s_tcp.connect((self.host, self.port))
        print(f'[*] Connected to {self.host} on port {self.port}.')
        print('Type \'q\' to quit.')
        message = str(input('-> '))
        while message != 'q':
            #print(type(message))
            #print(message)
            convert_to_bytes = str.encode(message)
            #print(convert_to_bytes) # Python3 requires bytes to be sent - hack it for now but fix later to something cleaner
            message = convert_to_bytes
            self.s_tcp.send(message)
            data = self.s_tcp.recv(1024)
            decode_from_bytes = data.decode()
            data = decode_from_bytes
            print(f'Received from server: {data}')
            message = str(input('-> '))
        self.s_tcp.close()

    def udp_server(self) -> None:
        """UDP server that binds to user provided host and port."""
        self.s_udp.bind((self.host, self.port))
        print(
            f'[*] UDP Server binding to {self.host}, listening on port {self.port}.')
        while True:
            data, address = self.s_udp.recvfrom(1024)
            if not data:
                break
            decode_from_bytes = data.decode()
            data = decode_from_bytes
            data = str(data).upper()
            print(
                f'[*] From connected User {address[0]} on port {address[1]}, message:\n {data}')
            if data == 'Q':
                self.s_udp.sendto('Server disconnected.', address)
                self.s_udp.close()
                return
            self.s_udp.sendto(str.encode('ACK'), address)
        self.s_udp.close()

    def udp_client(self) -> None:
        """UDP client to connect to a UDP server."""
        address = (self.host, 9099)
        server = (self.host, self.port)
        self.s_udp.bind(address)
        print('[*] Type \'q\' to quit.')
        message = input('-> ')
        while message != 'q':
            convert_to_bytes = str.encode(message)
            message = convert_to_bytes
            self.s_udp.sendto(message, server)
            data, address = self.s_udp.recvfrom(1024)
            print(
                f'[*] Received from server {self.host}, listening on port {self.port}:\n {data}')
            message = input('-> ')
        convert_to_bytes = str.encode(message)
        message = convert_to_bytes
        self.s_udp.sendto(message, server)
        data, address = self.s_udp.recvfrom(1024)
        print(
            f'[*] Received from server {self.host}, listening on port {self.port}:\n {data}')
        self.s_udp.close()

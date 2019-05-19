#!/usr/bin/python3

import argparse, socket
from datetime import datetime

MAX_BYTES = 65535
SERVER_ADDRESS = '127.0.0.1'


def server(address=SERVER_ADDRESS, port=4000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((address, port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)


def client(address=SERVER_ADDRESS, port=4000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.bind((address, port))
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, (address, port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send or receive UDP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-a', metavar='ADDR', default=SERVER_ADDRESS, help='UDP ADDR (default {})'.format(SERVER_ADDRESS))
    parser.add_argument('-p', metavar='PORT', type=int, default=4000, help='UDP port (default 4000)')
    args = parser.parse_args()
    function = choices[args.role]
    print(args.a)
    function(args.a, args.p)



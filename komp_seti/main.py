import argparse

from komp_seti.UDP.UDPClient import client
from komp_seti.UDP.UDPServer import server


def args_command():
    parser = argparse.ArgumentParser()
    parser.add_argument("protocol", type=str, nargs='*', help="")
    parser.add_argument("type", type=str, help="")
    args = parser.parse_args()

    if args.type == 'server':
        server()

    if args.type == 'client':
        client()



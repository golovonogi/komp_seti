import argparse

from komp_seti.TCP.TCPClent import tcp_client
from komp_seti.TCP.TCPServer import tcp_server
from komp_seti.UDP.UDPClient import udp_client
from komp_seti.UDP.UDPServer import udp_server


def args_command():
    parser = argparse.ArgumentParser()
    parser.add_argument("protocol", type=str, help="")
    parser.add_argument("type", type=str, help="")
    args = parser.parse_args()

    if args.protocol == 'udp':
        if args.type == 'server':
            udp_server()

        if args.type == 'client':
            udp_client()

    if args.protocol == 'tcp':
        if args.type == 'server':
            tcp_server()

        if args.type == 'client':
            tcp_client()

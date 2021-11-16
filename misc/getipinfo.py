#!/usr/bin/python3

# getipinfo PYTHON EDITION!!!!
# qorg and perl BTFO

# This script resolves an IPv4 or IPv6 address and passes it to ipinfo.io
# to get information about that IP. You can pass -6 to force IPv6.

# Usage: getipinfo HOSTNAME

# Where hostname can be a domain name or an IPv4 or IPv6 address.

from argparse import ArgumentParser
from socket import getaddrinfo, AF_INET, AF_INET6
from requests import get
from os.path import basename
from sys import exit

parser = ArgumentParser()
parser.add_argument("hostname")
vers = parser.add_mutually_exclusive_group()
vers.add_argument("-4", action="store_const", const=AF_INET, help="use IPv6")
vers.add_argument("-6", action="store_const", const=AF_INET6, help="use IPv6")
args = parser.parse_args()

try:
    opts = (args.hostname, 0, (vars(args)['4'] or vars(args)['6']) or 0)
    address = getaddrinfo(*opts)[-1][-1][0]
except Exception as e:
    print(f"{basename(__file__)}: error: {e.__class__.__name__} {e}")
    exit(1)

try:
    ip_info = get(f"https://ipinfo.io/{address}").json()
    print("ip:",       ip_info["ip"])
    print("city:",     ip_info["city"])
    print("region:",   ip_info["region"])
    print("country:",  ip_info["country"])
    print("timezone:", ip_info["timezone"])
    print("org:",      ip_info["org"])
    print("hostname:", ip_info["hostname"])
except Exception as e:
    print(f"{basename(__file__)}: error: {e.__class__.__name__} {e}")
    exit(1)

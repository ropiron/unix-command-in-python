#!/usr/bin/env python3

# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("echo")
# args=parser.parse_args()
# print(args.echo)

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

import argparse
import fileinput
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-d","--delimeter", default=" ", help="-d --delimeter")
parser.add_argument("-f","--field", help="-f --fields",type=int,nargs=2)
parser.add_argument('file', nargs='?', type=argparse.FileType('r'),default=sys.stdin)
args = parser.parse_args()

F=args.file
print(args)

#!/usr/bin/env python3

import argparse
import fileinput

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--lines", help="-n --lines",type=int)
    parser.add_argument("-c","--byte", help="-c --bytes",type=int)
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args()
    a=args.lines
    b=args.byte
    c=args.filenames

    for line in fileinput.input(a):
        pass
    print(fileinput.lineno())

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import argparse
import fileinput

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--lines", default=10, help="-n --lines",type=int)
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args()
    a=args.lines
    b=args.filenames

    for line in fileinput.input(b):
        if(not(fileinput.lineno()>a)):
            print(line)
        else:
            break

if __name__ == "__main__":
    main()

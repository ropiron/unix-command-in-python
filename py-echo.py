#!/usr/bin/env python3

import argparse
from sys import stdin, stdout, argv
# import sys

def main():
    for arg in argv[1:]:
        print(arg, end="")

if __name__ == "__main__":
    main()

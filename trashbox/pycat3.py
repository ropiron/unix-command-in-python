#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        with open(arg, 'rb') as f:
            sys.stdout.buffer.write(f.read())

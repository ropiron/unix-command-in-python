#!/usr/bin/env python3
from sys import stdin, stdout, argv

CHUNK_SIZE=2**10


if __name__ == '__main__':
    def copy_to_stdout(f):
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            stdout.buffer.write(chunk)

    if len(argv) == 0:
        copy_to_stdout(stdin.buffer)
    else:
        for arg in argv[1:]:
            with open(arg, 'rb') as f:
                copy_to_stdout(f)

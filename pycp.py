#!/usr/bin/env python3

import os
import argparse
import fileinput
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*',type=str)
    parser.add_argument('dirnames', nargs='*',type=str)
    # parser.add_argument("-r","--recursive", default=" ", help="-r --recursive")
    args = parser.parse_args()
    a=args.filenames[0]
    b=args.filenames[1]
    with fileinput.input(a) as f:
        if os.path.isfile(a):
            shutil.copy(a,b)
        else:
            shutil.copytree(a,b)
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# import argparse
# import fileinput

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-d","--delimiter", default=" ", help="-d --delimiter")
#     parser.add_argument("-f","--field", help="-f --fields",type=int,nargs=2)
#     parser.add_argument('filenames', nargs='*')
#     args = parser.parse_args()
#     a=args.field[0]
#     b=args.field[1]
#     d=args.delimiter
#     with fileinput.input(args.filenames) as f:
#         def process(fp,d,a,b):
#             for line in fp:
#                 f=line.split(d)
#                 print(d.join(f[a-1:b]), end='')
#         process(f,d,a,b)

# if __name__ == "__main__":
#     main()

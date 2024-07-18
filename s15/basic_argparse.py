
# import sys

# # print(sys.argv)
# print(sum(map(int,sys.argv[1:])))


import argparse


arg_parser = argparse.ArgumentParser(description="a simple argparse")
arg_parser.add_argument("n",type=int,help="define number n")
arg_parser.add_argument("m",type=int,help="define number m")
arg_parser.add_argument("--knum",type=int,help="define number k")


args = arg_parser.parse_args()

print(args)
print(args.n)
print(args.m)
print(args.knum)
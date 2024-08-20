#!/usr/bin/env python3

import argparse

# create an argument parser object
parser = argparse.ArgumentParser()

# Define some arguments
parser.add_argument('-a')
parser.add_argument('-b')
parser.add_argument('-c')

# Parse the user's arguments (in sys.args) according to the rules/args that we defined
args = parser.parse_args()

# print the args namespace object that we got
print(args)

# all of the arguments are now available as attributes on the "args" object
print(f'{args.a=}')
print(f'{args.b=}')
print(f'{args.c=}')

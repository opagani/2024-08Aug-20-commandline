#!/usr/bin/env python3

import argparse

# create an argument parser object
parser = argparse.ArgumentParser()

# Define some arguments
parser.add_argument('-a', '--apple')
parser.add_argument('-b', '--banana')
parser.add_argument('-c', '--cucumber')

# Parse the user's arguments (in sys.args) according to the rules/args that we defined
args = parser.parse_args()

# print the args namespace object that we got
print(args)

# all of the arguments are now available as attributes on the "args" object
print(f'{args.apple=}')
print(f'{args.banana=}')
print(f'{args.cucumber=}')

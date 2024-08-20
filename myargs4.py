#!/usr/bin/env python3

import argparse

# create an argument parser object
parser = argparse.ArgumentParser()

# Define some arguments
parser.add_argument('-n', '--number', type=int, default=10)
parser.add_argument('-f', '--file', type=argparse.FileType('r'))

# Parse the user's arguments (in sys.args) according to the rules/args that we defined
args = parser.parse_args()

# Now I can open the file, and read "args.number" characters from it
print(open(args.file, 'r').read(args.number))

#!/usr/bin/env python3

import argparse
import glob
import os

# create an argument parser object
parser = argparse.ArgumentParser()

# Define some arguments
parser.add_argument('--dirname', type=str)
parser.add_argument('--text', type=str)

# Parse the user's arguments (in sys.args) according to the rules/args that we defined
args = parser.parse_args()

# Now I can open the file, and read "args.number" characters from it

for one_filename in glob.glob(f'{args.dirname}/*'):
    if os.isfile(one_filename):
        for one_line in open(one_filename):
            if args.text in one_line:
                print(one_line)

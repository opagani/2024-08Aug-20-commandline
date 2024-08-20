#!/usr/bin/env python3

import argparse
import glob

# create an argument parser object
parser = argparse.ArgumentParser()

# Define some arguments
parser.add_argument('--dirname', type=str)
parser.add_argument('--text', type=str)

# Parse the user's arguments (in sys.args) according to the rules/args that we defined
args = parser.parse_args()

# Now I can open the file, and read "args.number" characters from it

for one_filename in glob.glob(f'{dirname}/*'):
    print(one_filename)

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
    if os.path.isfile(one_filename):
        try:
            for index, one_line in enumerate(open(one_filename), 1):
                if args.text in one_line:
                    print(f'{one_filename}:{index}: {one_line}', end='')
        except PermissionError as e:
            print(f'\tNo permission to open {one_filename}')
        except UnicodeDecodeError as e:
            print(f'\tNon-Unicode file {one_filename}')

#!/usr/bin/env python3

import argparse

# create an argument parser object
parser = argparse.ArgumentParser()

# Parse the user's arguments (in sys.args) according to the rules/args that we defined
args = parser.parse_args()

# print the args object that we got
print(args)

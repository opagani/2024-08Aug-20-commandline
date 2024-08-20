#!/usr/bin/env python3

import argparse

# create an argument parser object
parser = argparse.ArgumentParser()

# Define some arguments
parser.add_argument('-1', '--first', type=float)
parser.add_argument('-o', '--op', type=str, default='+')
parser.add_argument('-2', '--second', type=float)

# Parse the user's arguments (in sys.args) according to the rules/args that we defined
args = parser.parse_args()

# print the args namespace object that we got
print(args)

# all of the arguments are now available as attributes on the "args" object
print(f'{args.first=}')
print(f'{args.op=}')
print(f'{args.second=}')

# here, I can be confident that I got the arguments and got the operator
# and the args are both floats!

if args.op == '+':
    print(f'{args.first} {args.op} {args.second} = {args.first+args.second}')
elif args.op == '*':
    print(f'{args.first} {args.op} {args.second} = {args.first*args.second}')
else:
    print(f'Unknown operator')

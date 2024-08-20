#!/usr/bin/env python3

import sys

for index, one_arg in enumerate(sys.argv):
    print(f'{index}\t{one_arg}\t{type(one_arg)}')

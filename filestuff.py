#!/usr/bin/env python3

import cmd
import os

class Filestuff(cmd.Cmd):

    def do_length(self, line):
        if os.path.exists(line):
            print(os.stat(line).st_size)
        else:
            print(f'{line} does not exist; try again')

    def do_reverse(self, line):
        if line.count(' ') >= 1:
            infilename, outfilename = line.split(maxsplit=1)

            if os.path.exists(infilename):
                with open(outfilename, 'w') as outfile:
                    for one_line in open(infilename):
                        outfile.write(one_line[::-1])
            else:
                print(f'{infilename} does not exist; try again')
        else:
            print(f'Not enough arguments')


    def do_quit(self, line):
        return True

if __name__ == '__main__':
    Filestuff().cmdloop()

#!/usr/bin/env python3

import cmd
import os
import rich

class Filestuff(cmd.Cmd):

    def precmd(self, line):   # this function is run before any other fires; its return value replaces line
        return line.lower()

    def do_length(self, line):
        if os.path.exists(line):
            print(os.stat(line).st_size)
        else:
            rich.print(f'[red][bold]{line}[/bold] does not exist; try again[/red]')

    def do_reverse(self, line):
        if line.count(' ') >= 1:
            infilename, outfilename = line.split(maxsplit=1)

            if os.path.exists(infilename):
                with open(outfilename, 'w') as outfile:
                    for one_line in open(infilename):
                        outfile.write(one_line[::-1])
            else:
                rich.print(f'[red][bold]{infilename}[/bold] does not exist; try again[/red]')
        else:
            rich.print(f'[red]Not enough arguments[/red]')


    def do_quit(self, line):
        return True

if __name__ == '__main__':
    Filestuff().cmdloop()

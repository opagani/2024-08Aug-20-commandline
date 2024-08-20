#!/usr/bin/env python3

import cmd
import os

class Filestuff(cmd.Cmd):
    def do_length(self, line):
        if os.path.exists(line):
            print(os.stat(line).st_size)
        else:
            print(f'{line} does not exist; try again')

    def do_quit(self, line):
        return True

if __name__ == '__main__':
    Filestuff().cmdloop()

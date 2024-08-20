#!/usr/bin/env python3

import cmd
import os

class Filestuff(cmd.Cmd):
    def do_length(self, line):
        print(os.stat(line))

    def do_quit(self, line):
        return True

if __name__ == '__main__':
    Filestuff().cmdloop()

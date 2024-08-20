#!/usr/bin/env python3

import cmd

class MyMenu(cmd.Cmd):
    def do_hello(self, line):
        print(f'Hello, {line}!')


if __name__ == '__main__':
    MyMenu().cmdloop()

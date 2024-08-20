#!/usr/bin/env python3

import cmd

class MyMenu(cmd.Cmd):
    def do_hello(self, line):
        """Say hello to the world"""
        print(f'Hello, {line}!')

    def do_quit(self, line):
        print('Bye bye!')
        return True

    def do_EOF(self, line):
        print('Bye bye, weirdo old hacker!')
        return True


if __name__ == '__main__':
    MyMenu().cmdloop()

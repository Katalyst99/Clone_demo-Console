#!/usr/bin/python3
"""This is the module for the command interpreter entry point"""

import cmd

class HBNBCommand(cmd.Cmd):
    """The class for the console defined"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of file command to exit the program"""
        return True

    def emptyline(self):
        """Should not execute anything when an empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

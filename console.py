#!/usr/bin/python3
"""This is the module for the command interpreter entry point"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The class for the console defined"""
    prompt = '(hbnb) '
    c_cls = ['BaseModel']

    def do_create(self, line):
        """Creates a new instance of BaseModel, nd prints the id."""
        if line == '':
            print('** class name missing **')
        elif line not in self.c_cls:
            print("** class doesn't exist **")
        else:
            c_name = eval(line)
            instance = c_name()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints string rep of instance based on name and id"""

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

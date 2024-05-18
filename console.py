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
        if not line:
            print('** class name missing **')
        else:
            strings = line.split()
            if len(strings) == 1:
                if strings[0] not in self.c_cls:
                    print("** class doesn't exist **")
                else:
                    print('** instance id missing **')
                return

            c_name, id_inst = strings[0], strings[1]
            if c_name not in self.c_cls:
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(c_name, id_inst)
            inst = storage.all().get(key)
            if inst:
                print(inst)
            else:
                print('** no instance found **')

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

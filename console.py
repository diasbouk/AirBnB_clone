#!/usr/bin/python3

"""
Entry point of our console
the console
"""
import cmd
import sys

from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    Class representing the commandline prompt
    """

    prompt = "(hbnb) "

    def do_exit(self):
        """
        Stops the cmd loop
        """

    def emptyline(self):
        """Handles when user
        enters an empty line ."""
        print("")
        return 0

    def do_quit(self, arg):
        """Quits"""
        return True

    def do_EOF(self, arg):
        """Same thing as quit"""
        return True

    def do_create(self, arg):
        """creates A new instance of a class"""
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class dosen't exist **")
        else:
            newInstance = BaseModel()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, class_name, id):
        """Shows info of instance based
        on arguments
        """
        if class_name is None or class_name == "":
            print("** class name missing **")
        if class_name != "BaseModel":
            print("** class name dosen't exist **")
        if id == "" or id is None:
            print("** instance id missing **")
        else:
            for elem in storage.all():
                if elem.id == id:
                    print(elem.__str__)
                    break


if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/python3

"""
Entry point of our console
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
        """ Handles when user
        enters an empty line ."""
        print("")
        return 0

    def do_quit(self, arg):
        """ Quits """
        return True

    def do_EOF(self, arg):
        """  Same thing as quit """
        return True

    def do_create(self, arg):
        """ creates A new instance of a class """
        if arg ==  "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class name dosen't exist **")
        else:
            newInstance = BaseModel()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, *args):
        """ Shows info of instance based
        on arguments
        """
        if args[1] != "BaseModel":
            print("** class name dosen't exist **")
        if args[1] == "":
            print("** class name missing **")
        if args[2] == "":
            print("** instance id missing **")
        else:
            for elem in storage.all():
                if elem.id == args[2]:
                    print(elem.__str__)


            

if __name__ == "__main__":
    HBNBCommand().cmdloop()

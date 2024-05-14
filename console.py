#!/usr/bin/python3

"""
Entry point of our console
"""
import cmd
import sys


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

    def do_quit(self, arg):
        """ Quits """
        return True

    def do_EOF(self, arg):
        """ Same thing as quit """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

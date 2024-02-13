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

    prompt = "(hbnb)"

    def do_exit(self):
        """
        Stops the cmd loop
        """

if __name__ == "__main__":
    HBNBCommand().cmdloop()

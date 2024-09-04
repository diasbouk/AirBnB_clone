#!/usr/bin/python3

"""
    Imports and stuff
"""
from unittest import TestCase
from console import HBNBCommand


class TestConsole(TestCase):
    """ Docs for Test """

    def test_help(self):
        # To test help command
        file = open('file', 'r')
        out = open('out', 'a')
        console = HBNBCommand(stdin=file, stdout=out)
        console.use_rawinput = False
        console.cmdloop()
        out.close()
        out = open('out', 'r')
        print('------------------------------------------->')
        print(out.read())
        file.close()
        out.close()

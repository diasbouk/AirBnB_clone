#!/usr/bin/python3

"""
Import modules and stuff here
"""


import unittest
from console import HBNBCommand

cons = HBNBCommand()


class TestConsole(unittest.TestCase):
    # subClass of unittest to test console
    def test_prompt(self):
        # tests promtp
        self.assertEqual(cons.prompt, "(hbnb) ")

    def test_EOF(self):
        # tests if quit succeed
        self.assertTrue(cons.do_quit)

    def test_emptyline(self):
        # Tests if new line is entered
        pass


if __name__ == "__main__":
    unittest.main()

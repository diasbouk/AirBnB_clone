#!/usr/bin/python3

""" 
Import modules and stuff here
"""

import unittest
import console

cons = console.HBNBCommand()

class TestConsole(unittest.TestCase):
    # subClass of unittest to test console
    def test_prompt(self):
        # tests promtp
        self.assertEqual(cons.prompt, "(hbnb) ")

if __name__ == "__main__":
    unittest.main()

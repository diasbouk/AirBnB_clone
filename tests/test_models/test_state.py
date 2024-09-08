#!/usr/bin/python3

"""Imports , modules"""

from models.state import State
import unittest

class TestState(unittest.TestCase):
    """Test class for state"""
    def test_attrs(self):
        ins = State()
        self.assertIsInstance(ins.name, str)

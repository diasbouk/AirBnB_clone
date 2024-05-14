#!/usr/bin/env python3

""" Import modules and stuff"""
import unittest
from models.base_model import BaseModel


base = BaseModel()

class TestBaseModel(unittest.TestCase):
    """ Class to test Base Model
         subclassin TestCase"""

    def test_types(self):
        # Tests types of instances attrs
        self.assertIsInstance(type(base.id), str);

if __name__ == '__main__':
    unittest.main()

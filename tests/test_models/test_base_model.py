#!/usr/bin/python3

import unittest
from AirBnB_clone.models import *


def is_string(input):
    if type(input) == str:
        return True
    else:
        return False

class testBaseModel(unittest.TestCase):
    def test_created(self):
        result = base_model.BasModel.__str__()
        self.assertIsNotNone(result)
        is_it = is_string(result)
        self.assertTrue(is_it)

if __name__ == "__main__":
    unittest.main()

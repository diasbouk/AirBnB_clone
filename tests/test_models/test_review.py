#!/usr/bin/python3

"""Imports , modules"""

from models.review import Review
import unittest

class TestReview(unittest.TestCase):
    """Test class for review"""
    def test_attrs(self):
        ins = Review()
        self.assertIsInstance(ins.place_id, str)
        self.assertIsInstance(ins.user_id, str)
        self.assertIsInstance(ins.text, str)

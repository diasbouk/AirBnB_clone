#!/usr/bin/python3

"""Imports , modules"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test class for city module"""
    def test_attrs(self):
        instance = City()
        self.assertIsInstance(instance.name, str)
        self.assertIsInstance(instance.state_id, str)

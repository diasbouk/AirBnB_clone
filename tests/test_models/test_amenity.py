#!/usr/bin/python3
""" Imports """

from unittest import TestCase as Tst
from models.amenity import Amenity


class TestAmenity(Tst):
    """Test class for amenity"""
    def test_name(self):
        # tests name
        instance = Amenity()
        self.assertEqual(type(instance.name), str)

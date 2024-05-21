#!/usr/bin/python3
# Import modules and stuff here

import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestAmenity(unittest.TestCase):
    # Class to test place

    def setUp(self):
        pass

    def test_data(self):
        # test data and attrs 
        a1 = Amenity()
        self.assertEqual(type(a1.name), str)

if __name__ == "__main__":
    unittest.main()

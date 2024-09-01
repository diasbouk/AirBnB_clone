#!/usr/bin/python3
import unittest
import time
import json
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    # Tests for file_storage
    def test_attrs(self):
        new_instance = FileStorage()
        self.assertEqual(type(new_instance.all()), dict)


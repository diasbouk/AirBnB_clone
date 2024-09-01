#!/usr/bin/python3

# Docs for imports
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    # Class for Basemodel Tests
    def test_id(self):
        new_instance = BaseModel()
        self.assertEqual(type(new_instance.id), str)

    def test_times(self):
        new_instance = BaseModel()
        self.assertEqual(type(new_instance.created_at),
                         type(new_instance.updated_at))

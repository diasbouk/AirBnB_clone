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

    def test_string(self):
        new_instance = BaseModel()
        string = new_instance.__str__()
        expc = f"[BaseModel] ({new_instance.id}) {new_instance.__dict__}"
        self.assertEqual(type(string), str)
        self.assertEqual(string, expc)

    def test_to_dict(self):
        new_instance = BaseModel()
        new_dict = new_instance.to_dict()
        self.assertEqual(type(new_dict['created_at']), str)
        self.assertEqual(type(new_dict['updated_at']), str)

    def test_types(self):
        # Tests for types of class mems
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.id, str)
        self.assertIsInstance(new_instance.__str__(), str)

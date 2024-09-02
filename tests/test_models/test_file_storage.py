#!/usr/bin/python3
import unittest
import time
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    # Tests for file_storage

    def test_types(self):
        # Tests for types
        new_instance = FileStorage()
        self.assertEqual(type(new_instance.all()), dict)

    def test_new(self):
        # Tests for creating a new instance
        new_instance = FileStorage()
        all = new_instance.all()
        new_obj = BaseModel()
        new_instance.new(new_obj)
        self.assertTrue(new_obj.to_dict() in new_instance.all().values())

    def test_save(self):
        file_name = 'storage.json'
        os.remove('storage.json')
        new_instance = FileStorage()
        new_obj = BaseModel()
        new_instance.new(new_obj)
        new_instance.save()
        with open(file_name, 'r', encoding='utf-8') as f:
            self.assertEqual(new_instance.all(), json.loads(f.read()))

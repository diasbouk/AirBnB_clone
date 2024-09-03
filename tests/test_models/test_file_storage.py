#!/usr/bin/python3
import unittest
import time
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    # Tests for file_storage

    def test_instance(self):
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_file_path(self):
        try:
            self.assertTrue(type(FileStorage._FileStorage__file_path) is str)
        except Exception as Excep:
            fs = FileStorage()
            self.assertTrue(type(fs._FileStorage__file_path) is str)

    def test_objs(self):
        try:
            self.assertTrue(type(FileStorage._FileStorage__objects) is dict)
        except Exception as Excep:
            fs = FileStorage()
            self.assertTrue(type(fs._FileStorage__objects) is dict)

    def test_all(self):
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)

    def test_reload(self):
        fs = FileStorage()
        try:
            file_path = FileStorage._FileStorage__file_path
            self.assertTrue(type(file_path) is str)
        except Exception as Excep:
            pass
        try:
            os.remove(file_path)
        except Exception as Excep:
            pass
        try:
            self.assertIsInstance(fs._FileStorage__objects, dict)
            fs._FileStorage__objects.clear()
        except Exception as Excep:
            pass

        ids = []
        for i in range(10):
            bm = BaseModel()
            self.assertIsInstance(bm, BaseModel)
            bm.updated_at = datetime.now()
            self.assertIsInstance(bm.updated_at, datetime)
            self.assertIsInstance(bm.id, str)
            fs.new(bm)
            ids.append(bm.id)

        fs.save()
        try:
            fs._FileStorage__objects.clear()
        except Exception as Excep:
            pass
        fs.reload()
        all_reloaded = fs.all()
        self.assertIsInstance(all_reloaded, dict)
        self.assertEqual(len(all_reloaded.keys()), len(ids))
        for id in ids:
            self.assertTrue(
                all_reloaded.get(id)
                or all_reloaded.get("{}.{}".format("BaseModel", id))
            )
        try:
            os.remove(file_path)
        except Exception as e:
            pass

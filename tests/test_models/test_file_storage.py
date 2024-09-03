#!/usr/bin/python3
import unittest
import time
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """ Tests for FileStorage class """

    def test_instance(self):
        """ Tests for instances """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_file_path(self):
        """ Tests for file_path """
        try:
            self.assertTrue(type(FileStorage._FileStorage__file_path) is str)
        except Exception as Excep:
            fs = FileStorage()
            self.assertTrue(type(fs._FileStorage__file_path) is str)

    def test_objs(self):
        """ Tests for objects """
        try:
            self.assertTrue(type(FileStorage._FileStorage__objects) is dict)
        except Exception as Excep:
            fs = FileStorage()
            self.assertTrue(type(fs._FileStorage__objects) is dict)

    def test_all(self):
        """ Tests for all """
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)

    def test_reload(self):
        """ Tests for reload """
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
        objs_by_id = {}
        for i in range(10):
            bm = BaseModel()
            self.assertIsInstance(bm, BaseModel)
            bm.updated_at = datetime.now()
            self.assertIsInstance(bm.updated_at, datetime)
            self.assertIsInstance(bm.id, str)
            fs.new(bm)
            bm.save()
            ids.append(bm.id)
            objs_by_id[bm.id] = bm

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
        for id in ids:
            obj_reloaded = all_reloaded.get(id)
            if obj_reloaded is None:
                obj_reloaded = all_reloaded.get("{}.{}".format("BaseModel",
                                                               id))
            self.assertEqual(obj_reloaded.__class__.__name__, 'BaseModel')
            obj_created = objs_by_id[id]
            self.assertTrue(obj_reloaded.id == obj_created.id)
            self.assertTrue(obj_reloaded.created_at == obj_created.created_at)
            self.assertTrue(obj_reloaded.updated_at == obj_created.updated_at)

        try:
            os.remove(file_path)
        except Exception as e:
            pass

    def test_bm_dattime_conversion(self):
        """ Tests for datetime """
        bm_init = BaseModel()
        bm_init.save()
        try:
            bm = BaseModel(**bm_init.to_dict())
        except Exception as Excp:
            bm = None
        if bm is None or bm.id != bm_init.id:
            try:
                bm = BaseModel(bm_init.to_dict())
            except Exception as Excp:
                bm = None
        self.assertEqual(bm.id, bm_init.id)
        self.assertEqual(type(bm.created_at), datetime)
        self.assertTrue(bm.created_at.year == bm_init.created_at.year)
        self.assertTrue(bm.created_at.month == bm_init.created_at.month)
        self.assertTrue(bm.created_at.day == bm_init.created_at.day)
        self.assertTrue(bm.created_at.hour == bm_init.created_at.hour)
        self.assertTrue(bm.created_at.minute == bm_init.created_at.minute)

    def test_tmp_file_storage(self):
        """ Tests for file_storage """
        class TmpFileStorage(FileStorage):
            __file_path = None
            __objects = []

            def all(self):
                return {}

            def new(self, obj):
                pass

            def save(self, ojb=None):
                pass

            def reload(self):
                pass
if __name__ == '__main__':
    unittest.main()

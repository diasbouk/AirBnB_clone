#!/usr/bin/python3

# Docs for imports
import unittest
from copy import copy
from time import sleep
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test class for baseModel """

    def test_types(self):
        """ Tests for Types """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.id, str)
        self.assertIsInstance(new_instance.__str__(), str)
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

    def test_id(self):
        """ Tests for id """
        new_instance = BaseModel()
        new_instance2 = BaseModel()
        self.assertEqual(type(new_instance.id), str)
        self.assertEqual(type(new_instance2.id), str)
        self.assertNotEqual(new_instance.id, new_instance2.id)

    def test_times(self):
        """ Tests for times """
        new_instance = BaseModel()
        self.assertEqual(type(new_instance.created_at),
                         type(new_instance.updated_at))

    def test_string(self):
        """ Tests for __str__ """
        new_instance = BaseModel()
        string = new_instance.__str__()
        expc = f"[BaseModel] ({new_instance.id}) {new_instance.__dict__}"
        self.assertEqual(type(string), str)
        self.assertEqual(string, expc)

        bm = BaseModel()
        s_bm = str(bm)
        self.assertEqual(s_bm.split(" ")[0], '[BaseModel]')
        self.assertTrue(s_bm.split(" ")[1] == "({})".format(bm.id))

    def test_to_dict(self):
        """ Tests for to_dict """
        new_instance = BaseModel()
        new_dict = new_instance.to_dict()
        self.assertEqual(type(new_dict['created_at']), str)
        self.assertEqual(type(new_dict['updated_at']), str)
        bm = BaseModel()
        ##
        bm.updated_at = datetime.now()
        d_json = bm.to_dict()
        self.assertTrue(type(d_json) is dict)
        self.assertTrue(type(d_json['id']) is str)
        self.assertTrue(type(d_json['created_at']), str)
        self.assertTrue(type(d_json['__class__']) is str)
        self.assertTrue(d_json['__class__']) is str

    def test_save(self):
        """ Tests for save """
        new_instance = BaseModel()
        old_update = copy(new_instance.updated_at)
        new_instance.save()
        self.assertNotEqual(new_instance.updated_at, old_update)
        bm = BaseModel()
        bm.save()
        self.assertIsInstance(bm.updated_at, datetime)
        d_json = bm.to_dict()
        self.assertIsInstance(d_json, dict)
        self.assertIsInstance(d_json['updated_at'], str)

    def test_methods(self):
        """ Tests for methods """
        class bm(BaseModel):
            # Doc
            def __init__(self, *args, **kwargs):
                # constructor
                self.id = 'test'

            def __str__(self):
                return ('')

            def to_dict(self):
                return ({})

    def test_creation_emtpy(self):
        """ Tests for empty """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)
        self.assertNotEqual(bm1.id, bm2.id)

    def test_creation_from_dict(self):
        """ Tests for tmp """
        bm1 = BaseModel()
        bm2 = BaseModel(**bm1.to_dict())
        self.assertEqual(bm1.id, bm2.id)

    def tmp_base_model(self):
        """ Tests for tmp """
        class BaseModel(BaseModel):

            def save(self):
                self.updated_at = datetime.now()

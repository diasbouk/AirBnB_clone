#!/usr/bin/env python3

""" Import modules and stuff"""
from datetime import date, datetime
import unittest
import uuid
from models.base_model import BaseModel


base = BaseModel()


class TestBaseModel(unittest.TestCase):
    """Class to test Base Model
    subclassin TestCase"""

    def test_base_init_with_args(self):
        # Tests initializing base 2 diff way's
        base2_id = str(uuid.uuid4())
        base2_created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        base2 = BaseModel(
            id=base2_id, name="BASE_2", created_at=base2_created_at, random_arg="RANDOM"
        )

        self.assertEqual(type(base2.id), str)
        self.assertEqual(base2_id, base2.id)

    def test_types(self):
        # Tests types of instances attrs
        self.assertEqual(type(base.id), str)

    def test_times(self):
        # Tests created_at and updated_at times
        self.assertEqual(type(base.created_at), datetime)

    def test_class_str(self):
        # Tests __str__
        # self.assertEqual(
        # )
        self.assertIsInstance(base, BaseModel)

    def test_save(self):
        # Test if updated_at is changed
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)


if __name__ == "__main__":
    unittest.main()

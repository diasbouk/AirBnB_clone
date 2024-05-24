#!/usr/bin/python3

""" Import modules and stuff"""
from datetime import datetime
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
            id=base2_id,
            name="BASE_2",
            created_at=base2_created_at,
            random_arg="RANDOM"
        )

        self.assertEqual(type(base2.id), str)
        self.assertEqual(base2_id, base2.id)

    def test_types(self):
        # Tests types of instances attrs
        self.assertEqual(type(base.id), str)

    def test_times(self):
        # Tests created_at and updated_at times
        self.assertEqual(type(base.created_at), datetime)

    def test_str(self):
        self.assertTrue(type(base.__str__) != str)
        self.assertEqual(base.__str__(), "[{}] ({}) {}".format(
            base.__class__.__name__, base.id, base.__dict__))

    def test_save(self):
        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.to_dict(), object)
        self.assertTrue(obj.to_dict()[element] == obj.__dict__[element] for element in obj.__dict__)


if __name__ == "__main__":
    unittest.main()

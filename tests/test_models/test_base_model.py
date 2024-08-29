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

    def test_str(self):
        self.assertTrue(type(base.__str__) != str)
        self.assertEqual(
            base.__str__(),
            "[{}] ({}) {}".format(base.__class__.__name__, base.id, base.__dict__),
        )

        def test_to_dict(self):
            """Test method for dict"""
            b1 = BaseModel()
            b2_uuid = str(uuid.uuid4())
            b2 = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
            b1_dict = b1.to_dict()
            self.assertIsInstance(b1_dict, dict)
            self.assertIn("id", b1_dict.keys())
            self.assertIn("created_at", b1_dict.keys())
            self.assertIn("updated_at", b1_dict.keys())
            self.assertEqual(b1_dict["__class__"], type(b1).__name__)
            with self.assertRaises(KeyError) as e:
                b2.to_dict()

        def test_save(self):
            """Test method for save"""
            b = BaseModel()
            time.sleep(0.5)
            date_now = datetime.now()
            b.save()
            diff = b.updated_at - date_now
            self.assertTrue(abs(diff.total_seconds()) < 0.01)

            obj = BaseModel()
            self.assertEqual(str(obj), f"[BaseModel] ({obj.id}) {obj.__dict__}")
            old_time = obj.updated_at
            obj.save()
            new_time = obj.updated_at
            self.assertLess(old_time, new_time)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3

""" for models import """


import unittest
from models.user import User

user = User()

class testUserClass(unittest.TestCase):
    # Class to test User class
    def test_email(self):
        # tests email
        self.assertEqual(type(User.email), str)

    def test_password(self):
        # tests password
        self.assertEqual(type(User.password), str)

    def test_first_name(self):
        # tests fname
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        # tests lname
        self.assertEqual(type(User.last_name), str)

if __name__ == "__main__":
    unittest.main()

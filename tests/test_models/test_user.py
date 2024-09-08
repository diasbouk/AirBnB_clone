#!/usr/bin/python3

"""For import and stuff"""
from models.user import User
from unittest import TestCase

class TestUser(TestCase):
    # Class for User class tests
    def test_types(self):
        # testing attrs
        user = User()
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)

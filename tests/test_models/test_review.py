#!/usr/bin/python3
# Import modules and stuff here

import unittest


class TestReview(unittest.TestCase):
    # Class to test place
    def test_random(self):
        # test empty
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()

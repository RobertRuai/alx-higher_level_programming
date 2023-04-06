#!/usr/bin/python3
"""Unittest for max_integer([])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """runs tests on max_integer function"""

   
    def test_max_and_negative_ints(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 4, 3]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)

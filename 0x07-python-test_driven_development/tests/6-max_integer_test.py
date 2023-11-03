import unittest
"""
Unit test for the code
"""
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 10, 15, 71]), 71)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 10, 5, 7]), 10)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 4, 5, 2]), 10)

    def test_float_list(self):
        self.assertEqual(max_integer([12.54, 87.41, 22.04]), 87.41)

    def test_one_element_float_list(self):
        self.assertEqual(max_integer([12.56]), 12.56)

    def test_one_element_list(self):
        self.assertEqual(max_integer([12]), 12)

    def test_negative_values_ordered_list(self):
        self.assertEqual(max_integer([-10, -4, -5, -2]), -2)

    def test_negative_values_unordered_list(self):
        self.assertEqual(max_integer([-10, -41, -5, -12]), -5)

    def test_mixed_list(self):
        self.assertEqual(max_integer([-10, 5, 2, -17]), 5)

    def test_one_element_list(self):
        self.assertEqual(max_integer([-5.6, -14.5, -2.21, -15.4]), -2.21)

    def test_string_list(self):
        self.assertEqual(max_integer(["hi", "friend", "eat"]), "hi")

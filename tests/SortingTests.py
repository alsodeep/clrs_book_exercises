__author__ = 'Sergei Lysenko'

import unittest

from sorting.InsertionSort import *


class SortingTests(unittest.TestCase):
    def setUp(self):
        self.a = [31, 41, 59, 26, 41, 58]
        self.b = [1, 0, 1]

    def test_insertion_sorting(self):
        self.assertEqual(insertion_sort(self.a), [26, 31, 41, 41, 58, 59])

    def test_reverse_insertion_sorting(self):
        self.assertEqual(insertion_sort_reverse(self.a), [59, 58, 41, 41, 31, 26])

    def test_binary_addition(self):
        self.assertEqual(binary_addition(self.b, self.b), [0, 1, 0, 1])

__author__ = 'Sergei Lysenko'

import unittest

from sorting.InsertionSort import *


class SortingTests(unittest.TestCase):
    def test_insertion_sorting(self):
        a = [31, 41, 59, 26, 41, 58]
        self.assertEqual(insertion_sort(a), [26, 31, 41, 41, 58, 59])

    def test_reverse_insertion_sorting(self):
        a = [31, 41, 59, 26, 41, 58]
        self.assertEqual(insertion_sort_reverse(a), [59, 58, 41, 41, 31, 26])

    def test_binary_addition(self):
        a = [1, 0, 1]
        b = [1, 0, 1]
        self.assertEqual(binary_addition(a, b), [0, 1, 0, 1])

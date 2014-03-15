import random
import unittest

from . import sort


class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        xs = range(100)
        random.shuffle(xs)
        sort.insertion_sort(xs)
        self.assertEqual(xs, range(100))

    def test_selection_sort(self):
        xs = range(100)
        random.shuffle(xs)
        sort.selection_sort(xs)
        self.assertEqual(xs, range(100))

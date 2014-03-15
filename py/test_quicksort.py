import random
import unittest

from . import quicksort


class SortTestCase(unittest.TestCase):
    maxDiff = None

    def test_sort(self):
        xs = range(100)
        random.shuffle(xs)
        self.assertEqual(quicksort.sort(xs), sorted(xs))

    def test_in_place(self):
        xs = range(100)
        random.shuffle(xs)
        quicksort.in_place(xs)
        self.assertEqual(xs, range(100))

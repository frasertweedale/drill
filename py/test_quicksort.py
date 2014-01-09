import random
import unittest

from . import quicksort


class SortTestCase(unittest.TestCase):
    maxDiff = None

    def test_sorts(self):
        xs = range(100)
        random.shuffle(xs)
        self.assertEqual(quicksort.sort(xs), sorted(xs))

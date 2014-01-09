import random
import unittest

from . import heapsort


class SortTestCase(unittest.TestCase):
    maxDiff = None

    def test_sort(self):
        xs = range(100)
        random.shuffle(xs)
        self.assertEqual(heapsort.sort(xs), range(100))

import random
import unittest

from . import mergesort


class DownTestCase(unittest.TestCase):
    maxDiff = None

    def test_sorts(self):
        xs = range(100)
        random.shuffle(xs)
        self.assertEqual(mergesort.down(xs), sorted(xs))


class UpTestCase(unittest.TestCase):
    maxDiff = None

    def test_sorts(self):
        xs = range(127)
        random.shuffle(xs)
        mergesort.up(xs)
        self.assertEqual(xs, range(127))

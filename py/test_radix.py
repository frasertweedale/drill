import random
import unittest

from . import radix


class LSDTestCase(unittest.TestCase):
    def test_sort(self):
        xs = range(2 ** 16)
        random.shuffle(xs)
        self.assertEqual(radix.lsd(xs), range(2 ** 16))


class MSDTestCase(unittest.TestCase):
    def test_sort(self):
        xs = [str(x) for x in xrange(2 ** 10)]
        random.shuffle(xs)
        self.assertEqual(
            radix.msd(xs),
            sorted([str(x) for x in xrange(2 ** 10)])
        )

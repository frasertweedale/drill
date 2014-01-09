import random
import unittest

from . import priq


class MaxTestCase(unittest.TestCase):
    def test_priq(self):
        q = priq.Max()
        xs = range(100)
        random.shuffle(xs)
        for x in xs:
            q.insert(x)
        deleted = []
        while q:
            deleted.append(q.delete())
        self.assertEqual(deleted, list(reversed(sorted(xs))))


class MinTestCase(unittest.TestCase):
    def test_priq(self):
        q = priq.Min()
        xs = range(100)
        random.shuffle(xs)
        for x in xs:
            q.insert(x)
        deleted = []
        while q:
            deleted.append(q.delete())
        self.assertEqual(deleted, sorted(xs))

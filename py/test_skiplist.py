import random
import unittest

from . import skiplist


class SkiplistTestCase(unittest.TestCase):
    def test_only_inserted_values_are_in_list(self):
        l = skiplist.SkipList()
        xs = range(0, 2000, 2)  # only insert even keys
        random.shuffle(xs)
        for x in xs:
            l.insert(x)
        self.assertNotIn(-1, l)
        for x in range(2000, 4):
            if x % 2:
                self.assertNotIn(x, l)
            else:
                self.assertIn(x, l)
        self.assertNotIn(2000, l)

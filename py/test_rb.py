import random
import unittest

from . import rb


class RBTestCase(unittest.TestCase):
    def test_stores_values(self):
        xs = range(4096)
        random.shuffle(xs)
        t = rb.RB()
        for i in xs:
            t.put(str(i), i)
        for i in xs:
            self.assertEqual(t.get(str(i)), i)

    def test_raises_KeyError_if_key_not_in_tree(self):
        t = rb.RB()
        for i in range(15):
            t.put(str(i), i)
        with self.assertRaises(KeyError):
            t.get('16')

    def test_iter_iterates_kv_pairs_in_order(self):
        xs = range(100)
        random.shuffle(xs)
        t = rb.RB()
        for i in xs:
            t.put(str(i), i)
        self.assertEqual(
            [kv for kv in t],
            sorted((str(i), i) for i in xrange(100))
        )

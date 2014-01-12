import unittest

from . import oldest_unique

class OldestUniqueTestCase(unittest.TestCase):
    def test_oldest_unique(self):
        o = oldest_unique.OldestUnique()
        self.assertIsNone(o.query())
        o.feed('a')
        self.assertEqual(o.query(), 'a')
        o.feed('a')
        self.assertIsNone(o.query())
        o.feed('a')
        self.assertIsNone(o.query())
        for c in 'bcdefbce':
            o.feed(c)
        self.assertEqual(o.query(), 'd')

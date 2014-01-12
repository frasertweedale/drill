import unittest

from . import nlargest

class NLargestTestCase(unittest.TestCase):
    def test_nlargest(self):
        n5 = nlargest.NLargest(5)
        n3 = nlargest.NLargest(3)
        stream = [7, 8, 9, 3, 1, 5, 6, 3, 2, 6, 7, 3, 7, 9, 1, 10, 0, 1]
        for x in stream:
            n5.feed(x)
            n3.feed(x)
        self.assertEqual(n5.query(), [10, 9, 8, 7])
        self.assertEqual(n3.query(), [10, 9, 8])

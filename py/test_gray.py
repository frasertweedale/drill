import unittest

import gray


class BitflipTestCase(unittest.TestCase):
    def test_run(self):
        prev = None
        seen = set()
        w = 8
        hamming_compares = 0
        for cur in gray.run(w):
            if prev is not None:
                hamming_compares += 1
                self.assertEqual(hamming_distance(w, prev, cur), 1)
            seen.add(from_bits(w, cur))
            prev = cur
        self.assertEqual(hamming_compares, 2 ** w - 1)
        self.assertEqual(len(seen), 2 ** w)
        self.assertItemsEqual(seen, range(2 ** w))


def from_bits(w, s):
    n = 0
    for i in xrange(w):
        if s[w - 1 - i] == ord('1'):
            n += 2 ** i
    return n


def hamming_distance(w, a, b):
    dist = 0
    for i in xrange(w):
        if a[i] != b[i]:
            dist += 1
    return dist

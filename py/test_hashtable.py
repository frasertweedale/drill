import unittest

from . import hashtable


class HashTableTestCase(unittest.TestCase):
    def test_stores_values(self):
        t = hashtable.HashTable()
        for i in range(4096):
            t[str(i)] = i
        for i in range(4096):
            self.assertEqual(t[str(i)], i)

    def test_raises_KeyError_if_key_not_in_table(self):
        t = hashtable.HashTable()
        for i in range(15):
            t[str(i)] = i
        with self.assertRaises(KeyError):
            t['16']

import random
import unittest

from . import trie


class RWayTrieCase(unittest.TestCase):
    def test_stores_values(self):
        xs = range(4096)
        random.shuffle(xs)
        t = trie.RWayTrie()
        for i in xs:
            t.put(str(i), i)
        for i in xs:
            self.assertEqual(t.get(str(i)), i)

    def test_raises_KeyError_if_key_not_in_tree(self):
        t = trie.RWayTrie()
        for i in range(15):
            t.put(str(i), i)
        with self.assertRaises(KeyError):
            t.get('16')
        t = trie.RWayTrie()
        t.put('asdf', 1)
        with self.assertRaises(KeyError):
            t.get('a')


class TernarySearchTrieCase(unittest.TestCase):
    def test_stores_values(self):
        xs = range(4096)
        random.shuffle(xs)
        t = trie.TernarySearchTrie()
        for x in xs:
            t.put(str(x), x)
        for x in xs:
            self.assertEqual(t.get(str(x)), x)

    def test_raises_KeyError_if_key_not_in_tree(self):
        t = trie.TernarySearchTrie()
        for i in range(15):
            t.put(str(i), i)
        with self.assertRaises(KeyError):
            t.get('16')
        t = trie.RWayTrie()
        t.put('asdf', 1)
        with self.assertRaises(KeyError):
            t.get('a')

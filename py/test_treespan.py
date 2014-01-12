import unittest

from . import treespan

# max span is 6     o root
#                  / \
#                 o   o 5
#                    / \
#                 3 o   o 4
#                  /     \
#               1 o       o 2
#                /         \
#               o           o

class TreespanTestCase(unittest.TestCase):
    def test_treespan(self):
        leaf = treespan.Tree(None, None)
        t1 = treespan.Tree(leaf, None)
        t2 = treespan.Tree(None, leaf)
        t3 = treespan.Tree(t1, None)
        t4 = treespan.Tree(None, t2)
        t5 = treespan.Tree(t3, t4)
        root = treespan.Tree(leaf, t5)
        self.assertEqual(treespan.treespan(leaf), (0, 0, 0))
        self.assertEqual(treespan.treespan(t1), (1, 1, 0))
        self.assertEqual(treespan.treespan(t3), (2, 2, 0))
        self.assertEqual(treespan.treespan(t2), (1, 0, 1))
        self.assertEqual(treespan.treespan(t4), (2, 0, 2))
        self.assertEqual(treespan.treespan(t5), (6, 3, 3))
        self.assertEqual(treespan.treespan(root), (6, 1, 4))

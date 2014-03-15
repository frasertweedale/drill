import unittest

from . import treepath
from . import treespan


class TreepathTestCase(unittest.TestCase):
    def test_l_to_r_with_root_on_path(self):
        # path from 4 to 3 is [4, 2, 1, 3]
        #
        #           1
        #          / \
        #         2   3
        #        /     \
        #       4       5
        #
        t4 = treespan.Tree(None, None)
        t5 = treespan.Tree(None, None)
        t2 = treespan.Tree(t4, None)
        t3 = treespan.Tree(None, t5)
        t1 = treespan.Tree(t2, t3)
        self.assertEqual(treepath.treepath(t1, t4, t3), [t4, t2, t1, t3])

    def test_r_to_l_with_root_on_path(self):
        t4 = treespan.Tree(None, None)
        t5 = treespan.Tree(None, None)
        t2 = treespan.Tree(t4, None)
        t3 = treespan.Tree(None, t5)
        t1 = treespan.Tree(t2, t3)
        self.assertEqual(treepath.treepath(t1, t3, t4), [t3, t1, t2, t4])

    def test_l_to_r_with_root_not_on_path(self):
        #            o root
        #           / \
        #          o   o 5
        #             / \
        #          3 o   o 4
        #           /     \
        #        1 o       o 2
        #         /         \
        #        o           o
        leaf = treespan.Tree(None, None)
        t1 = treespan.Tree(leaf, None)
        t2 = treespan.Tree(None, leaf)
        t3 = treespan.Tree(t1, None)
        t4 = treespan.Tree(None, t2)
        t5 = treespan.Tree(t3, t4)
        root = treespan.Tree(leaf, t5)
        self.assertEqual(treepath.treepath(root, t1, t2), [t1, t3, t5, t4, t2])

    def test_r_to_l_with_root_not_on_path(self):
        leaf = treespan.Tree(None, None)
        t1 = treespan.Tree(leaf, None)
        t2 = treespan.Tree(None, leaf)
        t3 = treespan.Tree(t1, None)
        t4 = treespan.Tree(None, t2)
        t5 = treespan.Tree(t3, t4)
        root = treespan.Tree(leaf, t5)
        self.assertEqual(treepath.treepath(root, t2, t1), [t2, t4, t5, t3, t1])

import unittest

from . import heap


class MaxTestCase(unittest.TestCase):
    def test_new_heap_is_empty(self):
        h = heap.Max()
        self.assertFalse(h)

    def test_heap_is_not_empty_after_insert(self):
        h = heap.Max()
        h.insert(1)
        self.assertTrue(h)

    def test_delete_last_item_returns_it_and_leaves_heap_empty(self):
        h = heap.Max()
        h.insert(1)
        self.assertEqual(h.delete(), 1)
        self.assertFalse(h)

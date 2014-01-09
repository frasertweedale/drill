import unittest

from . import queue


class QueueTestCase(unittest.TestCase):
    def test_initial_queue_is_empty(self):
        self.assertTrue(queue.Queue().is_empty())

    def test_queue_is_not_empty_after_enqueue(self):
        q = queue.Queue()
        q.enqueue('a')
        self.assertFalse(q.is_empty())

    def test_enqueue_then_dequeue_gives_same_value(self):
        q = queue.Queue()
        q.enqueue('a')
        self.assertEqual(q.dequeue(), 'a')

    def test_queue_is_empty_after_enqueue_then_dequeue(self):
        q = queue.Queue()
        q.enqueue('a')
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_dequeued_values_are_in_order_of_enqueue(self):
        values = ['a', 'b', 'c']
        q = queue.Queue()
        for value in values:
            q.enqueue(value)
        outvalues = []
        for i in range(len(values)):
            outvalues.append(q.dequeue())
        self.assertEqual(outvalues, values)

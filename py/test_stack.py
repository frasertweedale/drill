import unittest

from . import stack


class StackTestCase(unittest.TestCase):
    def test_initial_stack_is_empty(self):
        self.assertTrue(stack.Stack().is_empty())

    def test_stack_is_not_empty_after_push(self):
        s = stack.Stack()
        s.push('a')
        self.assertFalse(s.is_empty())

    def test_push_then_pop_gives_same_value(self):
        s = stack.Stack()
        s.push('a')
        self.assertEqual(s.pop(), 'a')

    def test_stack_is_empty_after_push_then_pop(self):
        s = stack.Stack()
        s.push('a')
        s.pop()
        self.assertTrue(s.is_empty())

    def test_popped_values_are_in_reverse_order_of_push(self):
        values = ['a', 'b', 'c']
        s = stack.Stack()
        for value in values:
            s.push(value)
        outvalues = []
        for i in range(len(values)):
            outvalues.append(s.pop())
        self.assertEqual(outvalues, list(reversed(values)))

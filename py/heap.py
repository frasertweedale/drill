import functools
import operator


class _Heap(object):
    def __init__(self, op, items=None):
        # op should return true iff first operand has higher prio
        self.op = op
        self.heap = [None]
        if items is not None:
            self.heap.extend(items)
            for i in range((len(self.heap) - 1) / 2, 0, -1):
                self.sink(i)

    def insert(self, value):
        self.heap.append(value)
        self.swim(len(self.heap) - 1)

    def delete(self):
        self.swap(1, len(self.heap) - 1)
        deleted = self.heap.pop()
        self.sink(1)
        return deleted

    def __nonzero__(self):
        return len(self.heap) > 1

    def sink(self, i):
        if 2 * i < len(self.heap):
            j = 2 * i + 1
            if j >= len(self.heap) or self.op(self.heap[j - 1], self.heap[j]):
                j -= 1
            if self.op(self.heap[j], self.heap[i]):
                self.swap(i, j)
                self.sink(j)

    def swim(self, i):
        if i > 1 and self.op(self.heap[i], self.heap[i / 2]):
            self.swap(i / 2, i)
            self.swim(i / 2)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


Max = functools.partial(_Heap, operator.gt)
Min = functools.partial(_Heap, operator.lt)

import functools
import operator


class _Heap(object):
    def __init__(self, op, items=None):
        # op should return true iff first operand has higher prio
        self.op = op
        if items is not None:
            items.append(items[0])
            items[0] = None
            self.heap = items
            for i in range((len(items) - 1) / 2, 0, -1):
                self.sink(i)
        else:
            self.heap = [None]

    def insert(self, value):
        self.heap.append(value)
        self.swim(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 2:
            deleted = self.heap.pop()
        else:
            deleted = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.sink(1)
        return deleted

    def __nonzero__(self):
        return len(self.heap) > 1

    def sink(self, i):
        while 2 * i < len(self.heap):
            j = 2 * i
            if j < len(self.heap) - 1 and self.op(self.heap[j + 1], self.heap[j]):
                j += 1
            if self.op(self.heap[j], self.heap[i]):
                self.swap(i, j)
                i = j
            else:
                break

    def swim(self, i):
        while i > 1 and self.op(self.heap[i], self.heap[i / 2]):
            self.swap(i / 2, i)
            i /= 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


Max = functools.partial(_Heap, operator.gt)
Min = functools.partial(_Heap, operator.lt)

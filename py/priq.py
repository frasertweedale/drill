import heap


class _PriQ(object):
    def insert(self, x):
        self.heap.insert(x)

    def delete(self):
        return self.heap.delete()

    def __nonzero__(self):
        return bool(self.heap)


class Max(_PriQ):
    def __init__(self):
        self.heap = heap.Max()


class Min(_PriQ):
    def __init__(self):
        self.heap = heap.Min()

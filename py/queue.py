class Queue(object):
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        node = self.Node(value)
        if self.last:
            self.last.next = node
        self.last = node
        if not self.first:
            self.first = node

    def dequeue(self):
        node = self.first
        self.first = node.next
        if self.last is node:
            self.last = None
        return node.value

    def is_empty(self):
        return self.first is None

    def __nonzero__(self):
        return not self.is_empty()

class Stack(object):
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, value):
        node = self.Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        self.top = node.next
        return node.value

    def is_empty(self):
        return self.top is None

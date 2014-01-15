class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class NLargest:
    def __init__(self, n):
        self.n = n
        self.size = 0
        self.head = None
        self.tail = None

    def feed(self, x):
        if self.head and x > self.head.value:
            node = Node(x)
            node.next = self.head
            self.head.prev = node
            self.head = node
            if self.size == self.n:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.size += 1
        elif not self.head:
            node = Node(x)
            self.head = node
            self.tail = node
            self.size += 1

    def query(self):
        l = []
        node = self.head
        while node:
            l.append(node.value)
            node = node.next
        return l

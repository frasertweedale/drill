class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class OldestUnique:
    def __init__(self):
        self.uniq = {}
        self.seen = set()
        self.head = None
        self.tail = None

    def feed(self, value):
        if value in self.uniq:
            # unlink from list but leave in uniq dict
            node = self.uniq[value]
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
        elif value not in self.seen:
            node = Node(value)
            if self.head is None:
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
            self.head = node
            self.uniq[value] = node
            self.seen.add(value)

    def query(self):
        if self.tail is not None:
            return self.tail.value

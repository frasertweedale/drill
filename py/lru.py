class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return "Node({!r}, {!r})".format(self.key, self.value)


class LRU(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key):
        node = self.cache.get(key)
        if node:
            self.unlink(node)
            self.link(node)
        return node

    def put(self, node):
        if node.key in self.cache:
            value = node.value
            node = self.cache[node.key]
            node.value = value
        elif len(self.cache) >= self.max_size:
            evictee = self.tail
            self.unlink(evictee)
            del self.cache[evictee.key]
        self.unlink(node)
        self.link(node)
        self.cache[node.key] = node

    def link(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def unlink(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head is node:
            self.head = node.next
        if self.tail is node:
            self.tail = node.prev

    def __repr__(self):
        l = []
        node = self.head
        while node:
            l.append(node)
            node = node.next
        return "LRU({!r})".format(l)

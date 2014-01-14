import random


class SkipList:
    class Node:
        def __init__(self, h, k):
            self.k = k
            self.pointers = [None for x in xrange(h)]

        def __repr__(self):
            return "Node({}, {})".format(len(self.pointers), self.k)

    def __init__(self):
        self.max_height = 6
        self.sentinel = self.Node(self.max_height, None)

    def _path(self, k):
        node = self.sentinel
        path = []
        for i in xrange(self.max_height - 1, -1, -1):
            if node.pointers[i] is not None and node.pointers[i].k < k:
                node = node.pointers[i]
            path.append(node)
        return list(reversed(path))

    def insert(self, k):
        path = self._path(k)
        h = 1
        while random.randint(0, 1):
            h += 1
        if h > self.max_height:
            h = self.max_height
        new_node = self.Node(h, k)
        for i in xrange(h):
            new_node.pointers[i] = path[i].pointers[i]
            path[i].pointers[i] = new_node

    def __contains__(self, k):
        path = self._path(k)
        return path[0].pointers[0] is not None and path[0].pointers[0].k == k

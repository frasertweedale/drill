RED, BLACK = range(2)


class RB(object):
    class Node(object):
        def __init__(self, k, v):
            self.k = k
            self.v = v
            self.color = RED
            self.l = None
            self.r = None

        def __iter__(self):
            return RBIter(self)

    def __init__(self):
        self.root = None

    def put(self, k, v):
        self.root = self._put(self.root, k, v)

    def _put(self, node, k, v):
        if not node:
            return self.Node(k, v)
        lr = cmp(k, node.k)
        if lr < 0:
            node.l = self._put(node.l, k, v)
        elif lr > 0:
            node.r = self._put(node.r, k, v)
        else:
            node.v = v

        if self.is_red(node.r) and not self.is_red(node.l):
            node = self.rotate_left(node)
        if self.is_red(node.l) and self.is_red(node.l.l):
            node = self.rotate_right(node)
        if self.is_red(node.l) and self.is_red(node.r):
            self.flip(node)

        return node

    def is_red(self, node):
        return node and node.color == RED

    @staticmethod
    def rotate_left(node):
        red = node
        red.color = RED
        black = red.r
        black.color = BLACK
        red.r = black.l
        black.l = red
        return black

    @staticmethod
    def rotate_right(node):
        red = node
        red.color = RED
        black = red.l
        black.color = BLACK
        red.l = black.r
        black.r = red
        return black

    @staticmethod
    def flip(node):
        node.color = RED
        node.l.color = BLACK
        node.r.color = BLACK

    def get(self, k):
        node = self.root
        while node:
            lr = cmp(k, node.k)
            if lr < 0:
                node = node.l
            elif lr > 0:
                node = node.r
            else:
                return node.v
        raise KeyError

    def __iter__(self):
        return iter(self.root)


class RBIter:
    LT, EQ, GT = range(3)

    def __init__(self, tree):
        self.tree = tree
        self.l_iter = None
        self.r_iter = None
        self.state = self.LT

    def next(self):
        if self.state == self.LT:
            if not self.tree.l:
                self.state = self.EQ
            else:
                if not self.l_iter:
                    self.l_iter = iter(self.tree.l)
                try:
                    return next(self.l_iter)
                except StopIteration:
                    self.state = self.EQ
        if self.state == self.EQ:
            self.state = self.GT
            return self.tree.k, self.tree.v
        elif self.tree.r:
            if not self.r_iter:
                self.r_iter = iter(self.tree.r)
            return next(self.r_iter)
        else:
            raise StopIteration

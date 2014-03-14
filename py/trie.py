class RWayTrie(object):
    def __init__(self):
        self.v = None
        self.r = [None for r in xrange(256)]

    def put(self, k, v):
        if len(k) == 0:
            self.v = v
        else:
            if not self.r[ord(k[0])]:
                self.r[ord(k[0])] = RWayTrie()
            self.r[ord(k[0])].put(k[1:], v)

    def prefix(self, k):
        """Return true if k is a prefix or key in trie."""
        if len(k) == 0:
            return any(i for i in self.r)
        elif self.r[ord(k[0])] is not None:
            return self.r[ord(k[0])].prefix(k[1:])
        else:
            return False

    def get(self, k):
        if len(k) == 0:
            if self.v is not None:
                return self.v
            else:
                raise KeyError
        elif self.r[ord(k[0])] is not None:
            return self.r[ord(k[0])].get(k[1:])
        else:
            raise KeyError

    def __contains__(self, k):
        try:
            self.get(k)
            return True
        except KeyError:
            return False


class TernarySearchTrie(object):
    def __init__(self):
        self.k = None
        self.v = None
        self.lt = None
        self.eq = None
        self.gt = None

    def put(self, k, v):
        if self.k is None:
            self.k = k[0]
        if len(k) == 1 and self.k == k[0]:
            self.v = v
        else:
            ptr = cmp(self.k, k[0])
            if ptr < 0:
                self.lt = self.lt or TernarySearchTrie()
                self.lt.put(k, v)
            elif ptr > 0:
                self.gt = self.gt or TernarySearchTrie()
                self.gt.put(k, v)
            else:
                self.eq = self.eq or TernarySearchTrie()
                self.eq.put(k[1:], v)

    def get(self, k):
        if len(k) < 1:
            raise KeyError
        elif len(k) == 1 and self.k == k[0]:
            if self.v is not None:
                return self.v
            else:
                raise KeyError
        else:
            ptr = cmp(self.k, k[0])
            try:
                if ptr < 0:
                    return self.lt.get(k)
                elif ptr > 0:
                    return self.gt.get(k)
                else:
                    return self.eq.get(k[1:])
            except AttributeError:
                raise KeyError

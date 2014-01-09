class HashTable(object):
    class Node(object):
        def __init__(self, k, v):
            self.k = k
            self.v = v

        def __eq__(self, k):
            return self.k == k

    def __init__(self):
        self.n_buckets = 512
        self.buckets = [[] for i in range(self.n_buckets)]

    def __getitem__(self, k):
        h = hash(k) % self.n_buckets
        l = self.buckets[h]
        try:
            return l[l.index(k)].v
        except ValueError:
            raise KeyError

    def __setitem__(self, k, v):
        h = hash(k) % self.n_buckets
        l = self.buckets[h]
        try:
            l[l.index(k)].v = v
        except ValueError:
            l.append(self.Node(k, v))

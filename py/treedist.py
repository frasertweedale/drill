class Tree(object):
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


class Tree(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.left = None
        self.right = None

# global var to store max dist
max_dist = 0
max_nodes = None

def max_dist(tree):
    if tree.left is None:
        ldist = (0, None)
    else:
        ldist = max_depth(tree.left) + 1  # (dist, node)

    if tree.right is None:
        rdist = (0, None)
    else:
        rdist = max_depth(tree.right) + 1  # (dist, node)

    spandist = ldist[0] + rdist[0]
    if spandist > max_dist:
        max_dist = spandist
        max_nodes = (ldist[1], rdist[1])

    if ldist[0] > rdist[0]
        node_to_pass_up = ldist[1]
    else:
        node_to_pass_up = rdist[1]
    return (max(ldist, rdist), node_to_pass_up)

tree = Tree(1)
tree.left = Tree(2)

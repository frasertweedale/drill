class Tree:
    def __init__(self, l, r):
        self.l = l
        self.r = r


def treespan(tree):
    """Return max span of tree assuming all links have weight of 1."""
    if tree is None:
        return (0, 0, 0)
    lspan = 0
    ldepth = 0
    rspan = 0
    rdepth = 0
    if tree.l:
        lspan, lldepth, lrdepth = treespan(tree.l)
        ldepth = lldepth + 1
    if tree.r:
        rspan, rldepth, rrdepth = treespan(tree.r)
        rdepth = rrdepth + 1
    return max((lspan, rspan, ldepth + rdepth)), ldepth, rdepth

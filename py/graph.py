import functools
import itertools
import operator

from . import priq
from . import queue


class Digraph(object):
    """Undirected graph."""
    def __init__(self):
        self._adj = {}

    @property
    def V(self):
        return len(self._adj)

    @property
    def E(self):
        return sum(len(v) for v in self._adj.viewvalues())

    def add_edge(self, v, w):
        if v not in self._adj:
            self._adj[v] = []
        if w not in self._adj:
            self._adj[w] = []
        self._adj[v].append(w)

    def adj(self, v):
        return self._adj[v]

    def __iter__(self):
        return iter(self._adj.viewkeys())

    def reverse(self):
        g = type(self)()
        for v, adj in self._adj.viewitems():
            for w in adj:
                g.add_edge(w, v)
        return g


class Graph(Digraph):
    def add_edge(self, v, w):
        super(Graph, self).add_edge(v, w)
        super(Graph, self).add_edge(w, v)


class DFS(object):
    def __init__(self, graph, start, marked=None):
        self.marked = marked if marked is not None else set()
        self.edge_to = {}
        self._post = []
        self.dfs(graph, start)
        self.post = list(reversed(self._post))

    def dfs(self, graph, v):
        self.marked.add(v)
        for w in graph.adj(v):
            if w not in self.marked:
                self.dfs(graph, w)
                self.edge_to[w] = v
        self._post.append(v)

    def has_path_to(self, v):
        return v in self.marked

    def path_to(self, v):
        if self.has_path_to(v):
            path = []
            path.append(v)
            while self.edge_to.get(v) is not None:
                v = self.edge_to.get(v)
                path.append(v)
            return list(reversed(path))


class BFS(object):
    def __init__(self, graph, start):
        self.queue = queue.Queue()
        self.marked = set()
        self.dist_to = {}
        self.edge_to = {}
        self._init_start(start)
        while self.queue:
            v = self.queue.dequeue()
            self.marked.add(v)
            for w in graph.adj(v):
                if w not in self.marked:
                    self.queue.enqueue(w)
                    self.edge_to[w] = v
                    self.dist_to[w] = self.dist_to[v] + 1

    def _init_start(self, start):
        self.dist_to[start] = 0
        self.queue.enqueue(start)

    def has_path_to(self, v):
        return v in self.marked

    def path_to(self, v):
        if self.has_path_to(v):
            path = []
            path.append(v)
            while self.edge_to.get(v) is not None:
                v = self.edge_to.get(v)
                path.append(v)
            return list(reversed(path))

    def distance_to(self, v):
        return self.dist_to.get(v)


class MultiStartBFS(BFS):
    def _init_start(self, start):
        self.dist_to = {}
        for v in start:
            self.dist_to[v] = 0
            self.queue.enqueue(v)


class ConnectedComponents(object):
    def __init__(self, graph):
        self.cc = {}

        self.len = 0
        for v in range(graph.V):
            if v not in self.cc:
                self.dfs(graph, self.len, v)
                self.len += 1

    def dfs(self, graph, cc, v):
        self.cc[v] = cc
        for w in graph.adj(v):
            if w not in self.cc:
                self.dfs(graph, cc, w)

    def connected(self, v, w):
        return self.id(v) == self.id(w)

    def __len__(self):
        return self.len

    def id(self, v):
        """Component identifier for v."""
        return self.cc[v]


class StrongComponents(object):
    def __init__(self, graph):
        self.sc = {}
        marked = set()
        po = []
        for v in graph:
            if v not in po:
                po = DFS(graph.reverse(), v, marked=marked).post + po
        self.len = 0
        marked = set()
        for v in po:
            if v not in self.sc:
                for w in DFS(graph, v, marked=marked).post:
                    self.sc[w] = self.len
                self.len += 1

    def connected(self, v, w):
        return self.id(v) == self.id(w)

    def __len__(self):
        return self.len

    def id(self, v):
        """Component identifier for v."""
        return self.sc[v]


@functools.total_ordering
class Edge(object):
    def __init__(self, v, w, weight):
        self.v = min((v, w))
        self.w = max((v, w))
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return "Edge({}, {}, {})".format(self.v, self.w, self.weight)

    def __hash__(self):
        return hash((self.v, self.w, self.weight))


class EdgeWeightedGraph(object):
    def __init__(self):
        self.edges = {}

    def add_edge(self, edge):
        if edge.v not in self.edges:
            self.edges[edge.v] = set()
        if edge.w not in self.edges:
            self.edges[edge.w] = set()
        self.edges[edge.v].add(edge)
        self.edges[edge.w].add(edge)

    def adj(self, v):
        return self.edges.get(v)


class KruskalMST(object):
    def __init__(self, g):
        cc_by_vertex = {}
        ccs = []
        self.edges = set()
        sorted_edges = sorted(itertools.chain.from_iterable(g.edges.viewvalues()))
        for edge in sorted_edges:
            v, w, weight = edge.v, edge.w, edge.weight
            vcc = cc_by_vertex.get(v, -1)
            wcc = cc_by_vertex.get(w, -2)
            if cc_by_vertex.get(v, -1) != cc_by_vertex.get(w, -2):
                self.edges.add(edge)
                if vcc >= 0 and wcc >= 0:
                    # merge connected components
                    for i in ccs[wcc]:
                        cc_by_vertex[i] = vcc
                    ccs[vcc] |= ccs[wcc]
                elif vcc >= 0:
                    # add w to vcc
                    ccs[vcc].add(w)
                    cc_by_vertex[w] = vcc
                elif wcc >= 0:
                    # add v to wcc
                    ccs[wcc].add(v)
                    cc_by_vertex[v] = wcc
                else:
                    # new cc
                    cc_by_vertex[v] = len(ccs)
                    cc_by_vertex[w] = len(ccs)
                    ccs.append(set((v, w)))


class PrimMST(object):
    def __init__(self, g):
        self.edges = set()
        q = priq.Min()
        vertices = {0}
        for edge in g.adj(0):
            q.insert(edge)
        while q:
            edge = q.delete()
            if edge.v not in vertices or edge.w not in vertices:
                self.edges.add(edge)
                new_vertex = edge.v if edge.v not in vertices else edge.w
                new_edges = g.adj(new_vertex)
                vertices.add(new_vertex)
                for edge in new_edges:
                    if edge.v not in vertices or edge.w not in vertices:
                        q.insert(edge)

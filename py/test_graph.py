import unittest

from . import graph


class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.g = graph.Graph()
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 0)

    def test_can_iterate_over_added_edges_via_vertices(self):
        self.assertItemsEqual(self.g.adj(0), [1, 2])
        self.assertItemsEqual(self.g.adj(1), [2, 0])
        self.assertItemsEqual(self.g.adj(2), [0, 1])

    def test_iter_iterates_keys(self):
        self.assertItemsEqual(list(iter(self.g)), [0, 1, 2])


class GraphSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.g = graph.Graph()
        for v, w in [
            (0, 1), (0, 2), (0, 5), (0, 6),
            (3, 4), (3, 5),
            (4, 5), (4, 6),

            (7, 8),

            (9, 10), (9, 11), (9, 12),
            (11, 12),

            (13, 14), (14, 15), (15, 16)
        ]:
            self.g.add_edge(v, w)


class DFSTestCase(GraphSearchTestCase):
    def test_has_path_to_returns_true_for_connected_paths(self):
        dfs = graph.DFS(self.g, 0)
        self.assertTrue(dfs.has_path_to(5))
        self.assertFalse(dfs.has_path_to(8))
        self.assertFalse(dfs.has_path_to(12))

        dfs = graph.DFS(self.g, 7)
        self.assertFalse(dfs.has_path_to(5))
        self.assertTrue(dfs.has_path_to(8))
        self.assertFalse(dfs.has_path_to(12))

        dfs = graph.DFS(self.g, 9)
        self.assertFalse(dfs.has_path_to(5))
        self.assertFalse(dfs.has_path_to(8))
        self.assertTrue(dfs.has_path_to(12))

    def test_path_to_returns_path_from_start_to_v_if_such_path_exists(self):
        dfs = graph.DFS(self.g, 13)
        self.assertEqual(dfs.path_to(16), [13, 14, 15, 16])
        self.assertEqual(dfs.path_to(13), [13])

    def test_path_to_returns_None_if_no_such_path_exists(self):
        dfs = graph.DFS(self.g, 0)
        self.assertIsNone(dfs.path_to(12))


class BFSTestCase(GraphSearchTestCase):
    def test_has_path_to_returns_true_for_connected_paths(self):
        bfs = graph.BFS(self.g, 0)
        self.assertTrue(bfs.has_path_to(5))
        self.assertFalse(bfs.has_path_to(8))
        self.assertFalse(bfs.has_path_to(12))

        bfs = graph.BFS(self.g, 7)
        self.assertFalse(bfs.has_path_to(5))
        self.assertTrue(bfs.has_path_to(8))
        self.assertFalse(bfs.has_path_to(12))

        bfs = graph.BFS(self.g, 9)
        self.assertFalse(bfs.has_path_to(5))
        self.assertFalse(bfs.has_path_to(8))
        self.assertTrue(bfs.has_path_to(12))

    def test_path_to_returns_path_from_start_to_v_if_such_path_exists(self):
        bfs = graph.BFS(self.g, 13)
        self.assertEqual(bfs.path_to(16), [13, 14, 15, 16])
        self.assertEqual(bfs.path_to(13), [13])

    def test_path_to_returns_None_if_no_such_path_exists(self):
        bfs = graph.BFS(self.g, 0)
        self.assertIsNone(bfs.path_to(12))

    def test_distance_to_returns_distance_from_start_to_target(self):
        bfs = graph.BFS(self.g, 13)
        self.assertEqual(bfs.distance_to(13), 0)
        self.assertEqual(bfs.distance_to(16), 3)
        self.assertIsNone(bfs.distance_to(0))


class ConnectedComponentsTestCase(GraphSearchTestCase):
    def test_len_returns_number_of_connected_components(self):
        cc = graph.ConnectedComponents(self.g)
        self.assertEqual(len(cc), 4)

    def test_components_that_should_be_connected_are_and_share_id(self):
        cc = graph.ConnectedComponents(self.g)
        self.assertTrue(cc.connected(0, 6))
        self.assertEqual(cc.id(0), cc.id(6))
        self.assertTrue(cc.connected(7, 8))
        self.assertEqual(cc.id(7), cc.id(8))
        self.assertTrue(cc.connected(9, 12))
        self.assertEqual(cc.id(9), cc.id(12))
        self.assertTrue(cc.connected(13, 16))
        self.assertEqual(cc.id(13), cc.id(16))

    def test_components_that_should_not_be_connected_are_not_connected(self):
        cc = graph.ConnectedComponents(self.g)
        self.assertFalse(cc.connected(6, 7))
        self.assertFalse(cc.connected(8, 9))
        self.assertFalse(cc.connected(12, 13))
        self.assertFalse(cc.connected(16, 0))


class DigraphTestCase(unittest.TestCase):
    def setUp(self):
        self.g = graph.Digraph()
        self.g.add_edge(0, 1)
        self.g.add_edge(1, 2)
        self.g.add_edge(2, 0)
        self.g.add_edge(3, 4)

    def test_can_iterate_over_added_edges_via_vertices(self):
        self.assertItemsEqual(self.g.adj(0), [1])
        self.assertItemsEqual(self.g.adj(1), [2])
        self.assertItemsEqual(self.g.adj(2), [0])

    def test_iter_iterates_vertices(self):
        self.assertItemsEqual(list(iter(self.g)), [0, 1, 2, 3, 4])


class DigraphSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.g = graph.Digraph()
        self.g.add_edge(0, 1)
        self.g.add_edge(0, 5)
        self.g.add_edge(2, 0)
        self.g.add_edge(2, 3)
        self.g.add_edge(3, 2)
        self.g.add_edge(3, 5)
        self.g.add_edge(4, 2)
        self.g.add_edge(4, 3)
        self.g.add_edge(5, 4)
        self.g.add_edge(6, 0)
        self.g.add_edge(6, 4)
        self.g.add_edge(6, 8)
        self.g.add_edge(6, 9)
        self.g.add_edge(7, 6)
        self.g.add_edge(7, 9)
        self.g.add_edge(8, 6)
        self.g.add_edge(9, 10)
        self.g.add_edge(9, 11)
        self.g.add_edge(10, 12)
        self.g.add_edge(11, 4)
        self.g.add_edge(11, 12)
        self.g.add_edge(12, 9)


class DigraphDFSTestCase(DigraphSearchTestCase):
    def test_reaches_reachable_vertices_only(self):
        dfs = graph.DFS(self.g, 0)
        for v in range(6):
            self.assertTrue(dfs.has_path_to(v))
        for v in range(6, 13):
            self.assertFalse(dfs.has_path_to(v))

    def test_retuns_valid_paths_to_reachable_vertices(self):
        dfs = graph.DFS(self.g, 0)
        self.assertIn(dfs.path_to(2), [[0, 5, 4, 2], [0, 5, 4, 3, 2]])


class DigraphBFSTestCase(DigraphSearchTestCase):
    def test_reaches_reachable_vertices_only(self):
        bfs = graph.BFS(self.g, 0)
        for v in range(6):
            self.assertTrue(bfs.has_path_to(v))
        for v in range(6, 13):
            self.assertFalse(bfs.has_path_to(v))

    def test_retuns_valid_paths_to_reachable_vertices(self):
        bfs = graph.BFS(self.g, 0)
        self.assertEqual(bfs.path_to(2), [0, 5, 4, 2])

    def test_distance_to_returns_distance_from_start_to_target(self):
        bfs = graph.BFS(self.g, 0)
        self.assertEqual(bfs.distance_to(0), 0)
        self.assertEqual(bfs.distance_to(2), 3)


class MultiStartBFSTestCase(DigraphSearchTestCase):
    def test_finds_shortest_paths(self):
        bfs = graph.MultiStartBFS(self.g, [1, 7, 10])
        self.assertEqual(bfs.path_to(4), [7, 6, 4])
        self.assertEqual(bfs.path_to(5), [7, 6, 0, 5])
        self.assertEqual(bfs.path_to(12), [10, 12])


class StrongComponentsTestCase(DigraphSearchTestCase):
    def test_len_returns_number_of_connected_components(self):
        sc = graph.StrongComponents(self.g)
        self.assertEqual(len(sc), 5)

    def test_components_that_should_be_connected_are_and_share_id(self):
        sc = graph.StrongComponents(self.g)
        self.assertTrue(sc.connected(1, 1))
        self.assertEqual(sc.id(1), sc.id(1))
        self.assertTrue(sc.connected(0, 5))
        self.assertEqual(sc.id(0), sc.id(5))
        self.assertTrue(sc.connected(6, 8))
        self.assertEqual(sc.id(6), sc.id(8))
        self.assertTrue(sc.connected(7, 7))
        self.assertEqual(sc.id(7), sc.id(7))
        self.assertTrue(sc.connected(9, 12))
        self.assertEqual(sc.id(9), sc.id(12))

    def test_components_that_should_not_be_connected_are_not_connected(self):
        sc = graph.StrongComponents(self.g)
        self.assertFalse(sc.connected(1, 2))
        self.assertFalse(sc.connected(5, 6))
        self.assertFalse(sc.connected(6, 7))
        self.assertFalse(sc.connected(7, 9))
        self.assertFalse(sc.connected(12, 1))


class TopoTestCase(unittest.TestCase):
    def setUp(self):
        self.edges = {
            (0, 1),
            (0, 2),
            (0, 5),
            (1, 4),
            (3, 2),
            (3, 4),
            (3, 5),
            (3, 6),
            (5, 2),
            (6, 0),
            (6, 4),
        }
        self.g = graph.Digraph()
        for edge in self.edges:
            self.g.add_edge(*edge)

    def test_post_order_is_a_topological_order(self):
        dfs = graph.DFS(self.g, 3)
        seen = []
        for v in dfs.post:
            for w in seen:
                self.assertNotIn((v, w), self.edges)
            seen.append(v)
        self.assertItemsEqual(seen, dfs.post)


class MSTTestCase(unittest.TestCase):
    g = graph.EdgeWeightedGraph()
    edges = [graph.Edge(*args) for args in [
        (4, 5, 0.35),
        (4, 7, 0.57),
        (5, 7, 0.28),
        (0, 7, 0.16),
        (1, 5, 0.32),
        (0, 4, 0.38),
        (2, 3, 0.17),
        (1, 7, 0.19),
        (0, 2, 0.26),
        (1, 2, 0.36),
        (1, 3, 0.29),
        (2, 7, 0.34),
        (6, 2, 0.40),
        (3, 6, 0.52),
        (6, 0, 0.58),
        (6, 4, 0.93),
    ]]
    for edge in edges:
        g.add_edge(edge)
    mst_edges = [graph.Edge(*args) for args in [
        (0, 7, 0.16),
        (1, 7, 0.19),
        (0, 2, 0.26),
        (2, 3, 0.17),
        (5, 7, 0.28),
        (4, 5, 0.35),
        (6, 2, 0.40),
    ]]

    def test_kruskal_mst_determines_correct_edges(self):
        mst = graph.KruskalMST(self.g)
        self.assertItemsEqual(mst.edges, self.mst_edges)

    def test_prim_mst_determines_correct_edges(self):
        mst = graph.PrimMST(self.g)
        self.assertItemsEqual(mst.edges, self.mst_edges)

class ShortestPathsTestCase(unittest.TestCase):
    def test_shortest_path_returns_shortest_path(self):
        g = graph.EdgeWeightedGraph()
        for edge in [graph.Edge(*args) for args in [
            (4, 5, .35),
            (5, 5, .35),
            (4, 7, .37),
            (5, 7, .28),
            (7, 5, .28),
            (5, 1, .32),
            (0, 4, .38),
            (0, 2, .26),
            (7, 3, .39),
            (1, 3, .29),
            (2, 7, .34),
            (6, 2, .40),
            (3, 6, .52),
            (6, 0, .58),
            (6, 4, .93),
        ]]:
            g.add_edge(edge)
        return
        sp = graph.ShortestPaths(g, 0)
        self.assertItemsEqual(sp.path_to(6), [0, 2, 7, 3, 6])

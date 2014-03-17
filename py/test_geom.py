import unittest

from . import geom


class PointsFormSquareTestCase(unittest.TestCase):
    def test_points_form_square(self):
        points = [(1, 3), (1, 9), (7, 3), (7, 9)]
        self.assertTrue(geom.points_form_square(points))
        points = [(7, 9), (1, 9), (7, 3), (1, 3)]
        self.assertTrue(geom.points_form_square(points))
        points = [(7, 9), (1, 9), (7, 3), (2, 3)]
        self.assertFalse(geom.points_form_square(points))
        points = [(7, 9), (1, 8), (7, 3), (1, 2)]
        self.assertFalse(geom.points_form_square(points))
        points = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.assertTrue(geom.points_form_square(points))
        points = [(-1, 0), (0, -2), (1, 0), (0, 2)]
        self.assertFalse(geom.points_form_square(points))
        points = [(-1, 0), (0, -1), (1, 0), (1, 1)]
        self.assertFalse(geom.points_form_square(points))

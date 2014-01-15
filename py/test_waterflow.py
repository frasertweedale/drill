import unittest

from . import waterflow

#           (capacity is 5)
#       #
#     # #
#   # # #
#   ### # #
l = [2, 1, 3, 0, 4, 0, 1, 0]

#           (capacity is 9)
#         # #
#     #   ###
#   # # # ###
#   ### # ###
l2 = [2, 1, 3, 0, 2, 0, 4, 3, 4]


class WaterflowTestCase(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(waterflow.naive([]), 0)
        self.assertEqual(waterflow.naive(l), 5)
        self.assertEqual(waterflow.naive(l2), 9)

    def test_beautiful(self):
        self.assertEqual(waterflow.beautiful([]), 0)
        self.assertEqual(waterflow.beautiful(l), 5)
        self.assertEqual(waterflow.beautiful(l2), 9)

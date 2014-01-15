import unittest

import threesum


class ThreesumTestCase(unittest.TestCase):
    def test_threesum(self):
        l = [-25, -10, -7, -3, 2, 4, 8, 10]
        self.assertItemsEqual(
            threesum.threesum(l),
            [{-10, 2, 8}, {-7, -3, 10}]
        )

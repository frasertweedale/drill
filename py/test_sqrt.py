import unittest

from . import sqrt


class SqrtTestCase(unittest.TestCase):
    def test_binary_search(self):
        self.assertAlmostEqual(sqrt.binary_search(100.0, 1e-8), 10)
        self.assertAlmostEqual(sqrt.binary_search(1.0, 1e-8), 1)
        self.assertAlmostEqual(sqrt.binary_search(0.01, 1e-8), .1)
        self.assertAlmostEqual(sqrt.binary_search(-109.0, 1e-8), -1)

    def test_newton(self):
        self.assertAlmostEqual(sqrt.newton(100.0, 1e-8), 10)
        self.assertAlmostEqual(sqrt.newton(1.0, 1e-8), 1)
        self.assertAlmostEqual(sqrt.newton(0.01, 1e-8), .1)

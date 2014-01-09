import unittest

from . import alphacode

class AlphacodeTestCase(unittest.TestCase):
    def test_run(self):
        self.assertEqual(alphacode.run("1"), set("a"))
        self.assertItemsEqual(
            alphacode.run("1123"),
            set(["aabc", "kbc", "alc", "aaw", "kw"])
        )

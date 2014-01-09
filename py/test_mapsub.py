import unittest

from . import mapsub


class MapsubTestCase(unittest.TestCase):
    def test_mapsub(self):
        self.assertItemsEqual(
            mapsub.mapsub({'f': ['F', '4'], 'b': ['B', '8']}, 'fab'),
            ['fab', 'Fab', '4ab', 'faB', 'FaB', '4aB', 'fa8', 'Fa8', '4a8']
        )

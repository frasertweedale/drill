import unittest

import comb


class MaskKCombForAllKTestCase(unittest.TestCase):
    def test_mask_k_comb_for_all_k(self):
        self.assertEqual(
            comb.mask_k_comb_for_all_k(('a', 'b', 'c')),
            {
                ('*', '*', '*'),
                ('*', '*', 'c'),
                ('*', 'b', '*'),
                ('*', 'b', 'c'),
                ('a', '*', '*'),
                ('a', '*', 'c'),
                ('a', 'b', '*'),
                ('a', 'b', 'c')
            }
        )

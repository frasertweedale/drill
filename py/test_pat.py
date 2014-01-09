import unittest

from . import pat


class PatTestCase(unittest.TestCase):
    def test_pat(self):
        self.assertTrue(pat.match('a*', ''))
        self.assertFalse(pat.match('.', ''))
        self.assertTrue(pat.match('ab*', 'a'))
        self.assertTrue(pat.match('a.', 'ab'))
        self.assertTrue(pat.match('a', 'a'))

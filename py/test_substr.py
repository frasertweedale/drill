import unittest

from . import substr


text = """
    In computer science, the Rabin-Karp algorithm is a string
    searching algorithm created by Michael Rabin and Richard Karp
    in 1987.
    """


class RabinKarpTestCase(unittest.TestCase):
    def test_when_single_keyword_present_returns_true(self):
        self.assertTrue(substr.rabin_karp(["Michael Rabin"], text))

    def test_when_single_keyword_absent_returns_false(self):
        self.assertFalse(substr.rabin_karp(["Donald Knuth"], text))

    def test_when_any_of_multiple_keywords_present_returns_true(self):
        keywords = ["Donald Knuth", "Michael Rabin"]
        self.assertTrue(substr.rabin_karp(keywords, text))
        keywords = ["Richard Karp", "Michael Rabin"]
        self.assertTrue(substr.rabin_karp(keywords, text))

    def test_when_none_of_multiple_keywords_present_returns_false(self):
        keywords = ["Donald Knuth", "James Morris"]
        self.assertFalse(substr.rabin_karp(keywords, text))

    def test_checks_full_match_of_keyword_truncated_for_hash(self):
        keywords = ["ninechars", "only5"]
        self.assertTrue(substr.rabin_karp(keywords, "a ninechars match"))
        self.assertFalse(substr.rabin_karp(keywords, "a ninec*hars fail"))
        self.assertFalse(substr.rabin_karp(keywords, "a ninechar$ fail"))

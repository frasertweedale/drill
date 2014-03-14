import unittest

import sentence


class SentenceTestCase(unittest.TestCase):
    def test_add_spaces(self):
        self.assertEqual(
            sentence.add_spaces(
                "iamastudentfromwaterloo",
                {
                    "from", "waterloo", "hi", "am", "yes",
                    "i", "a", "student"
                }
            ),
            "i am a student from waterloo"
        )
        self.assertEqual(
            sentence.add_spaces(
                "asteroidsasaservice",
                {"service", "as", "asteroids", "a"}
            ),
            "asteroids as a service"
        )
        self.assertEqual(
            sentence.add_spaces(
                "shesellsseashellsbytheseashore",
                {
                    "she", "sells", "sea", "shells", "by",
                    "the", "shore"
                }
            ),
            "she sells sea shells by the sea shore"
        )

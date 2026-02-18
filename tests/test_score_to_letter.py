import unittest
from src.fundamentals.branching.score_to_letter import score_to_letter


class TestScoreToLetter(unittest.TestCase):

    def test_boundaries(self):
        self.assertEqual(score_to_letter(100), "A")
        self.assertEqual(score_to_letter(90), "A")
        self.assertEqual(score_to_letter(89), "B")
        self.assertEqual(score_to_letter(80), "B")
        self.assertEqual(score_to_letter(79), "C")
        self.assertEqual(score_to_letter(70), "C")
        self.assertEqual(score_to_letter(69), "D")
        self.assertEqual(score_to_letter(60), "D")
        self.assertEqual(score_to_letter(59), "F")
        self.assertEqual(score_to_letter(0), "F")

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            score_to_letter(-1)
        with self.assertRaises(ValueError):
            score_to_letter(101)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            score_to_letter(95.0)  # type: ignore
        with self.assertRaises(TypeError):
            score_to_letter("95")  # type: ignore


if __name__ == "__main__":
    unittest.main()

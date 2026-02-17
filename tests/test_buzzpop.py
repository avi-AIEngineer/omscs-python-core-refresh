
import unittest
from src.fundamentals.iteration.buzzpop import buzzpop


class TestBuzzPop(unittest.TestCase):

    def test_buzzpop_15(self):
        out = buzzpop(15)
        self.assertEqual(out[2], "Buzz")       # 3
        self.assertEqual(out[4], "Pop")        # 5
        self.assertEqual(out[14], "BuzzPop")   # 15
        self.assertEqual(len(out), 15)

    def test_zero(self):
        self.assertEqual(buzzpop(0), [])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            buzzpop("10")  # type: ignore

    def test_negative(self):
        with self.assertRaises(ValueError):
            buzzpop(-1)


if __name__ == "__main__":
    unittest.main()

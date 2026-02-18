import unittest
from src.fundamentals.collections.unique_keep_order import unique_keep_order


class TestUniqueKeepOrder(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(unique_keep_order([1, 2, 1, 3, 2]), [1, 2, 3])

    def test_strings(self):
        self.assertEqual(unique_keep_order(["a", "b", "a", "c", "b"]), ["a", "b", "c"])

    def test_empty(self):
        self.assertEqual(unique_keep_order([]), [])

    def test_none_raises(self):
        with self.assertRaises(TypeError):
            unique_keep_order(None)  # type: ignore


if __name__ == "__main__":
    unittest.main()

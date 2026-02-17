import unittest
from fundamentals.branching.pal_check import check_palindrome


class TestPalCheck(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(check_palindrome("Madam"), "Palindrome")

    def test_not_palindrome(self):
        self.assertEqual(check_palindrome("Hello"), "Not Palindrome")

    def test_empty(self):
        self.assertEqual(check_palindrome("   "), "Empty input")

    def test_none_raises(self):
        with self.assertRaises(TypeError):
            check_palindrome(None)  # type: ignore


if __name__ == "__main__":
    unittest.main()

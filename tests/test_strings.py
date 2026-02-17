import unittest
from src.fundamentals.basics.strings import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome("Madam"))

    def test_phrase(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Hello"))

    def test_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_numbers(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12310"))

    def test_none_raises(self):
        with self.assertRaises(TypeError):
            is_palindrome(None)

if __name__ == "__main__":
    unittest.main()

import unittest
from src.fundamentals.collections.token_counter import token_counter


class TestTokenCounter(unittest.TestCase):

    def test_basic_sentence(self):
        text = "To be, or not to be."
        self.assertEqual(token_counter(text), {
            "to": 2,
            "be": 2,
            "or": 1,
            "not": 1
        })

    def test_case_and_punctuation(self):
        self.assertEqual(token_counter("Hello, HELLO!! hello."), {"hello": 3})

    def test_numbers(self):
        self.assertEqual(token_counter("A1 a1 A1!!"), {"a1": 3})

    def test_empty(self):
        self.assertEqual(token_counter(""), {})

    def test_none_raises(self):
        with self.assertRaises(TypeError):
            token_counter(None)  # type: ignore


if __name__ == "__main__":
    unittest.main()

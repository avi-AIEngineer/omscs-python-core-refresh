
import re


def is_palindrome(s: str) -> bool:
    if s is None:
        raise TypeError("Input cannot be None")

    normalized = re.sub(r"[^a-z0-9]", "", s.lower())
    return normalized == normalized[::-1]

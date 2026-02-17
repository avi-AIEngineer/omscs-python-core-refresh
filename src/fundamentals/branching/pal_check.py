from src.fundamentals.basics.strings import is_palindrome


def check_palindrome(text: str) -> str:
    """
    Branching exercise:
    Returns a classification string based on palindrome check.
    """
    if text is None:
        raise TypeError("text cannot be None")

    if text.strip() == "":
        return "Empty input"

    if is_palindrome(text):
        return "Palindrome"
    return "Not Palindrome"


if __name__ == "__main__":
    user_input = input("Enter text: ")
    print(check_palindrome(user_input))

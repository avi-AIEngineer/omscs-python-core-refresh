def score_to_letter(score: int) -> str:
    """
    Convert a numeric score (0-100) to a letter grade.

    90-100: A
    80-89 : B
    70-79 : C
    60-69 : D
    0-59  : F
    """
    if not isinstance(score, int):
        raise TypeError("score must be an int")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    raw = input("Enter score (0-100): ").strip()
    try:
        s = int(raw)
        print(score_to_letter(s))
    except Exception as e:
        print(f"Error: {e}")

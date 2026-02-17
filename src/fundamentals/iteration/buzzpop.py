def buzzpop(n: int) -> list[str]:
    """
    Return a list of strings from 1..n with:
    - "BuzzPop" for multiples of 3 and 5
    - "Buzz" for multiples of 3
    - "Pop" for multiples of 5
    - otherwise the number as a string
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be >= 0")

    out: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("BuzzPop")
        elif i % 3 == 0:
            out.append("Buzz")
        elif i % 5 == 0:
            out.append("Pop")
        else:
            out.append(str(i))
    return out

import re


def token_counter(text: str) -> dict[str, int]:
    """
    Count word-like tokens in text (case-insensitive), ignoring punctuation.
    Example: "To be, or not to be." -> {"to": 2, "be": 2, "or": 1, "not": 1}
    """
    if text is None:
        raise TypeError("text cannot be None")

    tokens = re.findall(r"[a-z0-9]+", text.lower())
    counts: dict[str, int] = {}
    for tok in tokens:
        counts[tok] = counts.get(tok, 0) + 1
    return counts

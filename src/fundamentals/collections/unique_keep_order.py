from typing import Iterable, TypeVar, List

T = TypeVar("T")


def unique_keep_order(items: Iterable[T]) -> List[T]:
    """
    removes\ duplicates from a sequence but keep the original order of first appearance.
    Works for hashable items.
    Example: [1,2,1,3,2] -> [1,2,3]
    """
    if items is None:
        raise TypeError("items cannot be None")

    seen: set[T] = set()
    out: List[T] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

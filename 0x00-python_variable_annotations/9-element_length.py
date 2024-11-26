#!/usr/bin/env python3
"""Annotated function"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculates a length of all elements inside a list.

    Args:
        lst (Iterable[Sequence]): the list of elements.

    Returns:
        List[Tuple[Sequence, int]]: list of tuples with element and lenght.
    """
    return [(i, len(i)) for i in lst]

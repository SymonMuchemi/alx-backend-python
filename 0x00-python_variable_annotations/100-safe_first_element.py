#!/usr/bin/env python3
"""Annotated function"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the list if it exists, otherwise return None.
    Args:
        lst (Sequence): A sequence (e.g., list, tuple).
    Returns:
        Union[Any, None]: The first element | None.
    """

    if lst:
        return lst[0]
    else:
        return None

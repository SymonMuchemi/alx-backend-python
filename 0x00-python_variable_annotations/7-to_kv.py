#!/usr/bin/env python3
"""to_kv module"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """Takes a string and a float/int and return a tuple
    of the string with the number squared as a float.

    Args:
        k (str): The string.
        v (Union[float, int]): Float or integer number.

    Returns:
        tuple: result.
    """
    return (k, float(v**2))

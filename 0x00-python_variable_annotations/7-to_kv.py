#!/usr/bin/env python3
from typing import Union


def to_kv(k: str, v: Union[float, int]) -> tuple:
    """Takes a string and a float/int and return a tuple
    of the string with the number squared.

    Args:
        k (str): The string.
        v (Union[float, int]): Float or integer number.

    Returns:
        tuple: result.
    """
    return (k, v**2)
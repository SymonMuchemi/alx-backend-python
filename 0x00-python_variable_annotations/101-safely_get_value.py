#!/usr/bin/env python3
"""Uses TypeVar"""


from typing import TypeVar, Union, Any, Mapping


T = TypeVar('T')
d = Union[T, None]
u = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: d = None) -> u:
    """Safely retrieves the value of a key.

    Args:
        dct (Mapping): Mapping
        key (Any): Key to retrieve value with.
        default (Union[T, None], optional): Default value. Defaults to None.

    Returns:
        Union[Any, T]: The value returned or any.
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""Type checking"""

from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """Zooms an array

    Args:
        lst (Tuple[Any, ...]): Tuple list.
        factor (int, optional): Zoom factor. Defaults to 2.

    Returns:
        Tuple[Any, ...]: tuple.
    """
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

#!/usr/bin/env python3
"""Make multiplier module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function.

    Args:
        multiplier (float): Value to be squared.

    Returns:
        Callable[..., float]: a callable function that squares the multiplier.
    """
    def multiply(m: float) -> float:
        """squares the m value.

        Args:
            m (float): The value to be multiplied.

        Returns:
            float: m * m.
        """
        return float(multiplier**2)

    return multiply

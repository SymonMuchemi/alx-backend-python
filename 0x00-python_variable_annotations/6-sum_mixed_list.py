#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats and return their sum.

    Args:
        mxd_list (List[int, float]): Mixed list.

    Returns:
        float: Sum.
    """
    return sum(mxd_list)

#!/usr/bin/env python3
"""spawns wait_random several times"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """Returns a list of all delays in ascending order.

    Args:
        n (int): number of times to call wait_random.
        max_delay (float): The maximum duration of delay.

    Returns:
        List[float]: List of all the delays.
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))

    for i in range(len(delays)):
        for j in range(0, len(delays) - 1 - i):
            if delays[j] > delays[j + 1]:
                delays[j], delays[j + 1], delays[j + 1], delays[j]

    return delays

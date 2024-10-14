#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random value asynchronously.

    Args:
        max_delay (int, optional): Maximum delay. Defaults to 10.

    Returns:
        float: some random value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

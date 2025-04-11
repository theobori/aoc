#!/usr/bin/env pypy

import os
from collections import deque

with os.fdopen(0) as f:
    stones = map(int, f.read().split())


# Decorator stolen here https://flexiple.com/python/memoization-using-decorators-python
def memoize(func):
    cache = {}

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def blink(stone, blink_count):
    if blink_count == 0:
        return 1

    if stone == 0:
        return blink(1, blink_count - 1)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_half_size = len(stone_str) // 2
        left = int(stone_str[:stone_half_size])
        right = int(stone_str[stone_half_size:])

        return blink(left, blink_count - 1) + blink(right, blink_count - 1)
    else:
        return blink(stone * 2024, blink_count - 1)


total = 0
for stone in stones:
    total += blink(stone, 75)

print(int(total))

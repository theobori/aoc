#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    towels, designs = filter(lambda x: len(x) > 0, f.read().split("\n\n"))

towels = towels.split(", ")
designs = designs.split()

try:
    from functools import cache as memoize
except ImportError:
    # Better to use cache from functools if available
    # Not the case for pypy <= 3
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
def is_possible(design):
    total = 0
    if len(design) == 0:
        return True

    for towel in towels:
        if design.startswith(towel):
            total += is_possible(design[len(towel) :])

    return total


total = 0
for design in designs:
    total += is_possible(design)

print(total)

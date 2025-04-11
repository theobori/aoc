#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    towels, designs = filter(lambda x: len(x) > 0, f.read().split("\n\n"))

towels = towels.split(", ")
designs = designs.split()


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
    if len(design) == 0:
        return True

    for towel in towels:
        if design.startswith(towel):
            if is_possible(design[len(towel) :]):
                return True

    return False


total = 0
for design in designs:
    if is_possible(design) is True:
        total += 1

print(total)

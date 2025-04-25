#!/usr/bin/env pypy


import os


with os.fdopen(0) as f:
    schemes = filter(lambda el: len(el) > 0, f.read().split("\n\n"))


keys, locks = [], []
for scheme_str in schemes:
    heights = [0] * 5
    scheme = scheme_str.splitlines()
    is_lock = "#" in scheme[0]

    for line in scheme[1:] if is_lock else scheme[:-1]:
        for i in range(5):
            if line[i] == "#":
                heights[i] += 1

    heights = tuple(heights)
    if is_lock is True:
        locks.append(heights)
    else:
        keys.append(heights)


fits = 0
for key in keys:
    for lock in locks:
        if any(key[i] + lock[i] > 5 for i in range(5)):
            continue

        fits += 1

print(fits)

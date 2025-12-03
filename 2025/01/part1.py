#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [(x[0], int(x[1:])) for x in f.read().splitlines() if len(x) > 0]

dial = 50
ans = 0

for direction, distance in lines:
    if direction == "L":
        dial = (dial - distance) % 100
    elif direction == "R":
        dial = (dial + distance) % 100
    else:
        raise Exception("Unknown direction")

    if dial == 0:
        ans += 1

print(ans)

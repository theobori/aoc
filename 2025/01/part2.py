#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [(x[0], int(x[1:])) for x in f.read().splitlines() if len(x) > 0]

dial = 50
ans = 0

for direction, distance in lines:
    if direction == "L":
        delta = -1
    elif direction == "R":
        delta = 1
    else:
        raise Exception("Unknown direction")

    for _ in range(distance):
        dial += delta

        if dial == 0:
            ans += 1
        elif dial < 0:
            dial = 99
        elif dial >= 100:
            dial = 0
            ans += 1


print(ans)

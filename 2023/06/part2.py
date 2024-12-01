#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

table = []

for line in lines:
    table.append(int("".join(list(filter(lambda x: x.isdigit(), line.split(" "))))))

time, distance = table

possibilities = 0

for millisecond in range(time + 1):
    final = (time - millisecond) * millisecond

    if final > distance:
        possibilities += 1

print(possibilities)

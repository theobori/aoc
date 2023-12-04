#!/usr/bin/env python

with open("input.txt") as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

_sum = 0

for line in lines:
    line = list(filter(lambda x: x.isdigit(), line))
    
    if len(line) == 0:
        continue
    
    _sum += int("".join((line[0], line[-1])))

print(_sum)

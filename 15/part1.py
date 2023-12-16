#!/usr/bin/env pypy

with open(0) as f:
    steps = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split(",")
        )
    )

_sum = 0

for step in steps:
    v = 0
    
    for c in step:
        v = ((v + ord(c)) * 17) % 256

    _sum += v

print(_sum)

#!/usr/bin/env pypy

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n\n")
        )
    )

seeds = lines.pop(0)
_, seeds_values = seeds.split(": ")

seeds = list(map(int, seeds_values.split(" ")))

entries = []

for line in lines:
    line = filter(lambda x: len(x) > 0,line.split("\n")[1:])
    line = tuple(map(lambda x: tuple(map(int, x.split(' '))), line))

    entries.append(line)

def _next_value(_next: int, entry: tuple) -> int:
    for destination, source, length in entry:
        if length > 0:
            length -= 1

        if length <= 0:
            continue

        if source <= _next <= source + length:
            _next -= source - destination
            break
    
    return _next

lowest_location = -1

for seed in seeds:
    _next = seed

    for entry in entries:
        _next = _next_value(_next, entry)
    
    if lowest_location == -1 or _next < lowest_location:
        lowest_location = _next
    
print(lowest_location)

#!/usr/bin/env pypy

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

lines = list(map(list, lines))
rocks = [(y, x) for y, line in enumerate(lines) for x in range(len(line)) if line[x] == "O"]

_sum, height = 0, len(lines)

for y, x in rocks:
    ry = y
    
    while ry - 1 >= 0 and lines[ry - 1][x] == ".":
        ry -= 1
    
    lines[y][x] = "."
    lines[ry][x] = "O"
    
    _sum += height - ry

print(_sum)

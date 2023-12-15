#!/usr/bin/env pypy

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

empty_lines, empty_cols = [], []

is_empty = lambda c: c == "."

# fill empty lines
for y, line in enumerate(lines):
    if all(map(is_empty, line)):
        empty_lines.append(y)

# fill empty columns
for x in range(len(lines[0])):
    if all(map(is_empty, [line[x] for line in lines])):
        empty_cols.append(x)

# find galaxies
galaxies = [(y, x) for x in range(len(lines[y])) for y in range(len(lines)) if lines[y][x] == "#"]

# find pairs
_sum = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        ay, ax = galaxies[i]
        by, bx = galaxies[j]

        for line in range(min(ay, by), max(ay, by)):
            _sum += 1_000_000 if line in empty_lines else 1
        
        for col in range(min(ax, bx), max(ax, bx)):
            _sum += 1_000_000 if col in empty_cols else 1

print(_sum)

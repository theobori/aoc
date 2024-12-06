#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

TURNS = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


w, h = len(lines[0]), len(lines)
y, x, dy, dx = None, None, -1, 0

for i, line in enumerate(lines):
    if "^" in line:
        y, x = i, line.index("^")
        break

visited = set()
while y >= 0 and x >= 0 and y < h and x < w:
    if not (y, x) in visited:
        visited.add((y, x))

    if y + dy < h and x + dx < w and y + dy >= 0 and x + dx >= 0:
        if lines[y + dy][x + dx] == "#":
            dy, dx = TURNS[(dy, dx)]

    y += dy
    x += dx

print(len(visited))

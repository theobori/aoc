#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    grid = [list(line) for line in f.read().splitlines() if len(line) > 0]

n, m = len(grid), len(grid[0])
sx = grid[0].index("S")

grid[-1] = [1] * m

for y in range(n - 2, -1, -1):
    for x in range(m):
        if grid[y][x] == "^":
            grid[y][x] = grid[y + 1][x - 1] + grid[y + 1][x + 1]
        else:
            grid[y][x] = grid[y + 1][x]

print(grid[0][sx])

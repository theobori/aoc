#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    grid = [list(line) for line in f.read().splitlines() if len(line) > 0]

DELTAS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

n, m = len(grid), len(grid[0])
ans = 0

for y in range(n):
    for x in range(m):
        if grid[y][x] != "@":
            continue

        rolls_around = 0

        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if grid[ny][nx] == "@":
                rolls_around += 1

        if rolls_around < 4:
            ans += 1

print(ans)

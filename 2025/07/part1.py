#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    grid = [list(line) for line in f.read().splitlines() if len(line) > 0]

n, m = len(grid), len(grid[0])

st = deque()

for x in range(m):
    if grid[0][x] == "S":
        st.append((0, x))
        break

ans = 0
while st:
    y, x = st.pop()

    if grid[y][x] == "^":
        is_splitted = False

        if grid[y][x - 1] != "|":
            grid[y][x - 1] = "|"
            st.append((y, x - 1))
            is_splitted = True
        if grid[y][x + 1] != "|":
            grid[y][x + 1] = "|"
            st.append((y, x + 1))
            is_splitted = True

        if is_splitted:
            ans += 1
    else:
        grid[y][x] = "|"
        if y + 1 < m:
            st.append((y + 1, x))

print(ans)

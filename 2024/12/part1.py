#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

plots = map(list, lines)
w, h = len(plots[0]), len(plots)

plots_visited = [[False] * w for _ in range(h)]


def price(plots, plots_visited, y, x):
    area = 0
    perimeter = 0

    s = deque([(y, x)])

    category = plots[y][x]
    while s:
        y, x = s.pop()
        if plots_visited[y][x] is True:
            continue

        plots_visited[y][x] = True
        area += 1

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + dy
            nx = x + dx

            if ny < 0 or ny >= h or nx < 0 or nx >= w or plots[ny][nx] != category:
                perimeter += 1
            elif plots[ny][nx] == category and plots_visited[ny][nx] is False:
                s.append((ny, nx))

    return area * perimeter


total = 0
# Iterating throught the plots
for y in range(h):
    for x in range(w):
        # Check for an already visited plot
        if plots_visited[y][x] is True:
            continue
        total += price(plots, plots_visited, y, x)

print(total)

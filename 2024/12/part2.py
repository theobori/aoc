#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

plots = map(list, lines)
w, h = len(plots[0]), len(plots)

plots_visited = [[False] * w for _ in range(h)]


def create_region(plots, plots_visited, y, x):
    area = 0
    region = set()

    s = deque([(y, x)])

    category = plots[y][x]
    while s:
        y, x = s.pop()
        if plots_visited[y][x] is True:
            continue

        plots_visited[y][x] = True
        area += 1
        region.add((y, x))

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + dy
            nx = x + dx

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if plots[ny][nx] == category and plots_visited[ny][nx] is False:
                s.append((ny, nx))

    return area, region


def sides(region):
    total = 0

    for y, x in region:
        for ny, nx in (
            (1 + y, 1 + x),
            (-1 + y, -1 + x),
            (-1 + y, 1 + x),
            (1 + y, -1 + x),
        ):
            out_first = (ny, x)
            out_second = (y, nx)
            interior = (ny, nx)

            # Check for exterior corner
            if not out_first in region and not out_second in region:
                total += 1
            # Check for interior corner
            if out_first in region and out_second in region and not interior in region:
                total += 1

    return total


total = 0
for y in range(h):
    for x in range(w):
        if plots_visited[y][x] is True:
            continue
        area, region = create_region(plots, plots_visited, y, x)

        total += area * sides(region)


print(total)

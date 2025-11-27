#!/usr/bin/env pypy

import os
import heapq

from collections import deque

with os.fdopen(0) as f:
    maze = map(list, filter(lambda x: len(x) > 0, f.read().splitlines()))


w, h = len(maze[0]), len(maze)

initial_position = (0, 0)
for y in range(h):
    for x in range(w):
        if maze[y][x] == "S":
            initial_position = y, x
            break
    else:
        continue
    break


def best_sits(maze, initial_position, initial_delta):
    y, x = initial_position
    dy, dx = initial_delta

    s = [(0, y, x, dy, dx, set([y, x]))]
    visited = set([(y, x, dy, dx)])
    best = float("inf")

    sits = set()

    while s:
        score, y, x, _dy, _dx, positions = heapq.heappop(s)

        if maze[y][x] == "E":
            best = min(best, score)
            if score != best:
                continue

            sits = sits.union(positions)
            continue

        visited.add((y, x, _dy, _dx))

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx

            if (
                ny < 0
                or ny >= h
                or nx < 0
                or nx >= w
                or maze[ny][nx] == "#"
                or (ny, nx, dy, dx) in visited
            ):
                continue

            heapq.heappush(
                s,
                (
                    score + (1 if (_dy, _dx) == (dy, dx) else 1001),
                    ny,
                    nx,
                    dy,
                    dx,
                    set([(ny, nx)]).union(positions),
                ),
            )

    return len(sits) - 1


sits = best_sits(maze, initial_position, (0, 1))
print(sits)

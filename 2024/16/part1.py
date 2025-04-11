#!/usr/bin/env pypy

import os
import heapq

from collections import deque

with os.fdopen(0) as f:
    maze = map(list, filter(lambda x: len(x) > 0, f.read().splitlines()))


w, h = len(maze[0]), len(maze)


def find_start(maze):
    for y in range(h):
        for x in range(w):
            if maze[y][x] == "S":
                return y, x

    return 1, 1


initial_position = find_start(maze)


def best_score(maze, initial_position, initial_delta):
    y, x = initial_position
    dy, dx = initial_delta

    s = [(0, y, x, dy, dx)]
    visited = set([(y, x, dy, dx)])
    best = float("inf")

    while s:
        score, y, x, _dy, _dx = heapq.heappop(s)
        visited.add((y, x, _dy, _dx))

        if maze[y][x] == "E":
            best = min(best, score)
            break

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            if maze[ny][nx] == "#" or (ny, nx, dy, dx) in visited:
                continue

            nscore = score + (1 if (_dy, _dx) == (dy, dx) else 1001)
            heapq.heappush(s, (nscore, ny, nx, dy, dx))

    return best


score = best_score(maze, initial_position, (0, 1))
print(score)

#!/usr/bin/env pypy

import os
import heapq

from collections import deque

with os.fdopen(0) as f:
    corrupted_bytes = filter(lambda x: len(x) > 0, f.read().splitlines())

corrupted_bytes = map(lambda el: tuple(map(int, el.split(","))), corrupted_bytes)[:1024]

w, h = 71, 71
memory = [["."] * w for _ in range(h)]
for x, y in corrupted_bytes:
    memory[y][x] = "#"


start_x, start_y = 0, 0
target_position = (w - 1, h - 1)
visited = set()
heap = [(0, start_x, start_y)]
while heap:
    steps, x, y = heapq.heappop(heap)

    if (x, y) in visited:
        continue

    visited.add((x, y))

    if (x, y) == target_position:
        print(steps)
        break

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy

        if (
            nx < 0
            or nx >= w
            or ny < 0
            or ny >= h
            or memory[ny][nx] == "#"
            or (nx, ny) in visited
        ):
            continue

        heapq.heappush(heap, ((steps + 1, nx, ny)))

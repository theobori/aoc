#!/usr/bin/env pypy

import os
import heapq

from collections import deque

with os.fdopen(0) as f:
    corrupted_bytes = filter(lambda x: len(x) > 0, f.read().splitlines())

corrupted_bytes = map(lambda el: tuple(map(int, el.split(","))), corrupted_bytes)

w, h = 71, 71

start_x, start_y = 0, 0
target_position = (w - 1, h - 1)


def has_exit_path(byte_amount):
    memory = [["."] * w for _ in range(h)]
    for x, y in corrupted_bytes[:byte_amount]:
        memory[y][x] = "#"

    visited = set()
    heap = [(0, start_x, start_y, set([(start_x, start_y)]))]

    while heap:
        steps, x, y, path = heapq.heappop(heap)
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == target_position:
            return True

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

            heapq.heappush(heap, ((steps + 1, nx, ny, path.union([(nx, ny)]))))

    return False


left, right = 0, len(corrupted_bytes) - 1
while left < right:
    mid = (left + right) // 2

    has_exit = has_exit_path(mid + 1)

    if has_exit is True:
        left = mid + 1
    else:
        right = mid

mid = (left + right) // 2
print(corrupted_bytes[mid])

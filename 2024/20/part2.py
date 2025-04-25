#!/usr/bin/env pypy

import os

from collections import deque, defaultdict

with os.fdopen(0) as f:
    grid = map(list, filter(lambda x: len(x) > 0, f.read().splitlines()))


w, h = len(grid[0]), len(grid)


def find_position(grid, symbol):
    for y in range(h):
        for x in range(w):
            if grid[y][x] == symbol:
                return x, y


start = find_position(grid, "S")
end = find_position(grid, "E")


def path_positions(grid, start, end):
    start_x, start_y = start
    end_x, end_y = end

    # Should be in order
    positions = set()

    visited = set([(start_x, start_y)])

    s = deque([(start_x, start_y)])
    while s:
        x, y = s.pop()

        positions.add((x, y))
        if (x, y) == (end_x, end_y):
            break

        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if (
                nx < 0
                or nx >= w
                or ny < 0
                or ny >= h
                or grid[ny][nx] == "#"
                or (nx, ny) in visited
            ):
                continue

            visited.add((nx, ny))
            s.append((nx, ny))

    return positions


positions = path_positions(grid, start, end)

distances = {position: i for i, position in enumerate(positions)}


# Check in a circle around the location (x, y) with r=20
def count_picoseconds_saved(grid, distances, x, y, min_amount):
    total = 0
    distance_old = distances.get((x, y), 0)

    for dy in range(-20, 21):
        width = 20 - abs(dy)

        for dx in range(-width, width + 1):
            nx = x + dx
            ny = y + dy

            if (
                nx < 0
                or nx >= w
                or ny < 0
                or ny >= h
                or grid[ny][nx] == "#"
                or (nx == x and ny == y)
            ):
                continue

            distance_new = distances.get((nx, ny), 0)
            picoseconds_saved = distance_new - distance_old - abs(dy) - abs(dx)
            if picoseconds_saved >= min_amount:
                total += 1

    return total


total = sum(count_picoseconds_saved(grid, distances, x, y, 100) for x, y in distances)

print(total)

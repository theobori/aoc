#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

lines = map(list, lines)

TURNS = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


w, h = len(lines[0]), len(lines)
start_y, start_x, dy, dx = None, None, -1, 0


for i, line in enumerate(lines):
    if "^" in line:
        start_y, start_x = i, line.index("^")
        break


def is_infinite_loop(lines, y, x, dy, dx):
    cycle = 0

    while True:
        ny, nx = y + dy, x + dx

        if not (0 <= ny < h and 0 <= nx < w):
            return False

        if lines[ny][nx] == "#":
            dy, dx = TURNS[(dy, dx)]
            continue

        y, x = ny, nx

        if cycle == w * h:
            return True

        cycle += 1

    return False


out = 0
y, x = start_y, start_x

for y in range(h):
    for x in range(w):
        if lines[y][x] == ".":
            lines[y][x] = "#"

            if is_infinite_loop(lines, start_y, start_x, -1, 0) is True:
                out += 1

            lines[y][x] = "."

print(out)

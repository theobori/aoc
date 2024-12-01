#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

DIRECTIONS = {
    2: (0, -1),
    0: (0, 1),
    3: (-1, 0),
    1: (1, 0),
}

p = [0, 0]
points = [(0, 0)]
outline = 0

for line in lines:
    _, _, h = line.split()

    h = int(h[2:-1], 16)

    dir = h & 0b1111
    l = h >> 4

    dy, dx = DIRECTIONS[dir]
    l = int(l)

    p[0] += dy * l
    p[1] += dx * l

    outline += abs(dy * l) + abs(dx * l)

    points.append(tuple(p))

i, a = 0, 0

while i + 1 < len(points):
    y1, x1 = points[i]
    y2, x2 = points[i + 1]

    a += (y2 + y1) * (x1 - x2)

    i += 1

print((a // 2) + (outline // 2) + 1)

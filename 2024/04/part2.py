#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    m = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

OPPOSITE_DELTAS = (
    ((1, 1), (-1, -1)),
    ((-1, 1), (1, -1)),
)


def is_x_mas(m, pos, size):
    y, x = pos
    h, w = size

    if m[y][x] != "A":
        return 0

    for o in OPPOSITE_DELTAS:
        (fy, fx), (sy, sx) = o
        fy, fx = y + fy, x + fx
        sy, sx = y + sy, x + sx

        if fy < 0 or fx < 0 or sy < 0 or sx < 0:
            return False
        if fy >= h or fx >= w or sy >= h or sx >= w:
            return False

        first, second = m[fy][fx], m[sy][sx]

        if not first in "MS" or not second in "MS":
            return False
        if first == second:
            return False

    return True


out = 0
h, w = len(m), len(m[0])
for y in range(h):
    for x in range(w):
        out += is_x_mas(m, (y, x), (h, w))

print(out)

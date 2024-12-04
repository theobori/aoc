#!/usr/bin/env pypy

import os

DELTAS = (-1, 0, 1)
DIRECTIONS = [(y, x) for y in DELTAS for x in DELTAS if (y, x) != (0, 0)]

with os.fdopen(0) as f:
    m = list(filter(lambda x: len(x) > 0, f.read().splitlines()))


def count_xmas(m, pos, size):
    out = 0
    y, x = pos
    h, w = size

    for dy, dx in DIRECTIONS:
        ny, nx = y, x
        for c in "XMAS":
            if ny < 0 or nx < 0:
                break
            if ny >= h or nx >= w:
                break
            if m[ny][nx] != c:
                break

            ny += dy
            nx += dx
        else:
            out += 1

    return out


out = 0
h, w = len(m), len(m[0])
for y in range(h):
    for x in range(w):
        out += count_xmas(m, (y, x), (h, w))

print(out)

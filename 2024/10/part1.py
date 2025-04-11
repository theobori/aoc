#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

tmap = [list(map(int, line)) for line in lines]
w, h = len(tmap[0]), len(tmap)

# Retrieve every trailheads
trailheads = set()
for y in range(h):
    for x in range(w):
        if tmap[y][x] == 0:
            trailheads.add((y, x))


# Function that count the number of 9 a single trailhead can reach
def trailhead_score(tmap, trailhead):
    s = deque([trailhead])
    nines_visited = set()
    visited = set()
    score = 0

    while s:
        y, x = s.pop()
        number = tmap[y][x]

        if number == 9 and not (y, x) in nines_visited:
            nines_visited.add((y, x))
            score += 1

        visited.add((y, x))

        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = y + dy
            nx = x + dx

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            if tmap[ny][nx] != number + 1:
                continue

            if not (ny, nx) in visited:
                s.append((ny, nx))

    return score


total = sum(trailhead_score(tmap, trailhead) for trailhead in trailheads)

print(total)

#!/usr/bin/env pypy

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

DIRECTIONS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

p = [0, 0]
points = [(0, 0)]
outline = 0

for line in lines:
    d, l, _ = line.split()
    
    dy, dx = DIRECTIONS[d]
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

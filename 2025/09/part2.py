#!/usr/bin/env python

import os

from shapely import Polygon, box, BufferCapStyle

with os.fdopen(0) as f:
    reds = [
        list(map(int, line.split(",")))
        for line in f.read().splitlines()
        if len(line) > 0
    ]

n = len(reds)

polygon = Polygon(reds).buffer(0.55, cap_style=BufferCapStyle.square)

ans = float("-inf")

for i in range(n):
    x1, y1 = reds[i]

    for j in range(i + 1, n):
        x2, y2 = reds[j]

        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)

        square: Polygon = box(xmin, ymin, xmax, ymax).buffer(
            0.5, cap_style=BufferCapStyle.square
        )

        if polygon.contains(square):
            ans = max(ans, round(square.area))

print(ans)

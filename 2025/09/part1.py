#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    reds = [
        list(map(int, line.split(",")))
        for line in f.read().splitlines()
        if len(line) > 0
    ]


n = len(reds)

ans = float("-inf")

for i in range(n):
    xi, yi = reds[i][0], reds[i][1]

    for j in range(i + 1, n):
        xj, yj = reds[j][0], reds[j][1]

        w = abs(xj - xi) + 1
        h = abs(yj - yi) + 1

        area = w * h
        ans = max(ans, area)

print(ans)

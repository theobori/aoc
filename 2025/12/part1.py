#!/usr/bin/env python

import os


with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

n = len(lines)
i = 0
shapes = []
while i < n:
    line = lines[i]

    if line[-1] != ":":
        break

    i += 1

    count = 0
    while i < n and lines[i][0] in ".#":
        for ch in lines[i]:
            if ch == "#":
                count += 1

        i += 1

    shapes.append(count)

ans = 0

for j in range(i, n):
    line = lines[j]

    r_size, r_presents = line.split(": ")
    w, h = tuple(map(int, r_size.split("x")))
    r_presents = r_presents.split()

    area = w * h
    for shapes_i, quantity_str in enumerate(r_presents):
        quantity = int(quantity_str)

        area -= quantity * shapes[shapes_i]

        if area < 0:
            break
    else:
        ans += 1

print(ans)

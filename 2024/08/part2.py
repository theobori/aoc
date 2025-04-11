#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

city = [list(line) for line in lines]
w, h = len(city[0]), len(city)


def is_antenna(symbol):
    return symbol.isalnum()


antennas = []
for y in range(len(city)):
    line = city[y]
    for x in range(len(line)):
        symbol = city[y][x]
        if is_antenna(symbol) is True:
            antennas.append((symbol, y, x))

antinodes = 0
for i in range(len(antennas) - 1):
    si, yi, xi = antennas[i]
    for j in range(i + 1, len(antennas)):
        sj, yj, xj = antennas[j]
        if si != sj:
            continue

        dy = yi - yj
        dx = xi - xj
        y, x = yi, xi
        while y >= 0 and y < h and x >= 0 and x < w:
            if city[y][x] != "#":
                antinodes += 1
                city[y][x] = "#"
            y += dy
            x += dx

        dy = yj - yi
        dx = xj - xi
        y, x = yj, xj
        while y >= 0 and y < h and x >= 0 and x < w:
            if city[y][x] != "#":
                antinodes += 1
            city[y][x] = "#"
            y += dy
            x += dx

print(antinodes)

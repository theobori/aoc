#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    warehouse, moves = filter(lambda x: len(x) > 0, f.read().split("\n\n"))

warehouse = map(list, filter(lambda x: len(x) > 0, warehouse.splitlines()))
w, h = len(warehouse[0]), len(warehouse)

moves = moves.replace("\n", "")


def find_robot(warehouse):
    for y in range(h):
        for x in range(w):
            if warehouse[y][x] == "@":
                return y, x
    return 1, 1


ry, rx = find_robot(warehouse)

MOVE_DELTAS = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

for move in moves:
    dy, dx = MOVE_DELTAS[move]
    ny, nx = ry + dy, rx + dx

    if warehouse[ny][nx] == "#":
        continue

    if warehouse[ny][nx] == "O":
        oy, ox = ny, nx
        while warehouse[oy][ox] == "O":
            oy += dy
            ox += dx

        if warehouse[oy][ox] != ".":
            continue

        ty, tx = oy, ox
        oy, ox = ny, nx
        warehouse[oy][ox] = "."
        while (oy, ox) != (ty, tx):
            oy += dy
            ox += dx
            warehouse[oy][ox] = "O"

    warehouse[ry][rx] = "."
    warehouse[ny][nx] = "@"
    ry, rx = ny, nx

total = 0
for y in range(h):
    for x in range(w):
        if warehouse[y][x] == "O":
            total += y * 100 + x

print(total)

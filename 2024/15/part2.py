#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    warehouse, moves = filter(lambda x: len(x) > 0, f.read().split("\n\n"))

warehouse = filter(lambda x: len(x) > 0, warehouse.splitlines())

for i in range(len(warehouse)):
    warehouse[i] = list(
        warehouse[i]
        .replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )

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


# Move horizontal box
def mhb(warehouse, box, delta):
    by, bx = box
    dy, dx = delta

    while warehouse[by][bx] in "[]":
        bx += dx

    if warehouse[by][bx] == "#":
        return False

    tx = bx
    _, bx = box

    is_symbol_left = warehouse[by][bx] == "["

    warehouse[by][bx] = "."
    while bx != tx:
        bx += dx
        warehouse[by][bx] = "[" if is_symbol_left is True else "]"
        is_symbol_left ^= True

    return True


def _mvb(warehouse, box, delta, boxes):
    by, bx = box
    symbol = warehouse[by][bx]

    if symbol == "#":
        return False
    if symbol == ".":
        return True

    dy, dx = delta

    child_x = -1 if symbol == "]" else 1
    need_move = _mvb(warehouse, (by + dy, bx), delta, boxes) and _mvb(
        warehouse, (by + dy, bx + child_x), delta, boxes
    )
    if need_move is False:
        return False

    boxes.add((by, bx))
    boxes.add((by, bx + child_x))
    return True


# Move vertical box
def mvb(warehouse, box, delta):
    boxes = set()
    need_move = _mvb(warehouse, box, delta, boxes)

    if need_move is False:
        return False

    dy, _ = delta
    for by, bx in boxes:
        warehouse[by][bx], warehouse[by + dy][bx] = (
            warehouse[by + dy][bx],
            warehouse[by][bx],
        )

    return True


def move_boxes(warehouse, box, delta):
    dy, dx = delta

    if dx == 0:
        return mvb(warehouse, box, delta)

    if dy == 0:
        return mhb(warehouse, box, delta)

    return False


for move in moves:
    dy, dx = MOVE_DELTAS[move]
    ny, nx = ry + dy, rx + dx

    if warehouse[ny][nx] == "#":
        continue

    need_move = True
    if warehouse[ny][nx] in "[]":
        need_move = move_boxes(warehouse, (ny, nx), (dy, dx))

    if need_move is False:
        continue

    warehouse[ry][rx] = "."
    warehouse[ny][nx] = "@"
    ry, rx = ny, nx

total = 0
for y in range(h):
    for x in range(w):
        if warehouse[y][x] == "[":
            total += y * 100 + x


print(total)

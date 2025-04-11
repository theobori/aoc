#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    line = f.read().strip()

blocks = []

is_file = True
_id = 0
for symbol in line:
    number = int(symbol)

    if is_file is True:
        blocks.extend([_id] * number)
        _id += 1
    else:
        blocks.extend([None] * number)

    is_file ^= True

while None in blocks:
    cursor = blocks.index(None)
    elem = blocks.pop()
    if elem is None:
        continue

    if cursor < len(blocks):
        blocks[cursor] = elem

total = 0
for i in range(len(blocks)):
    total += i * blocks[i]

print(total)

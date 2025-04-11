#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    stones = map(int, f.read().split())

# Blinking 25 times
for blink_count in range(25):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            stone_str = str(stones[i])
            stone_half_size = len(stone_str) // 2
            left = int(stone_str[:stone_half_size])
            right = int(stone_str[stone_half_size:])

            stones[i] = left
            stones.insert(i + 1, right)
            i += 1
        else:
            stones[i] *= 2024
        i += 1

print(len(stones))

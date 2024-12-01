#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

height, width = len(lines), len(lines[0])

checks = ((-1, 0), (-1, -1), (0, -1), (-1, 1), (1, 0), (1, 1), (0, 1), (1, -1))

gears_coord = {}

for y, line in enumerate(lines):
    x = 0

    while x < len(line):
        size = 0
        is_valid_number = False
        number_x = x

        gear_coord = (-1, -1)

        while number_x < len(line) and line[number_x].isdigit():
            for dy, dx in checks:
                ny, nx = y + dy, number_x + dx

                if ny < 0 or ny >= height:
                    continue

                if nx < 0 or nx >= width:
                    continue

                char = lines[ny][nx]

                if not char.isdigit() and char == "*":
                    is_valid_number = True
                    gear_coord = (ny, nx)
                    break

            size += 1
            number_x += 1

        if is_valid_number == True:
            number = int(lines[y][number_x - size : number_x])

            if not gear_coord in gears_coord.keys():
                gears_coord[gear_coord] = [number]
            else:
                gears_coord[gear_coord].append(number)

            x += size

            continue

        x += 1

_sum = 0

for numbers in gears_coord.values():
    if len(numbers) != 2:
        continue

    gear_ratio = 1

    for number in numbers:
        gear_ratio *= number

    _sum += gear_ratio

print(_sum)

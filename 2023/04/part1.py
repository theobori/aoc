#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

to_integer = lambda x: list(map(int, filter(lambda y: len(y) > 0, x.split(" "))))

_sum = 0

for line in lines:
    _, numbers = line.split(":")

    winning_numbers, my_numbers = numbers.split("|")

    winning_numbers = to_integer(winning_numbers)
    my_numbers = to_integer(my_numbers)

    score = 0

    for my_number in my_numbers:
        if my_number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2

    _sum += score

print(_sum)

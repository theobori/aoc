#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

to_integer = lambda x: list(map(int, filter(lambda y: len(y) > 0, x.split(" "))))

_instances = [1] * len(lines)

for i, line in enumerate(lines):
    _, numbers = line.split(":")

    winning_numbers, my_numbers = numbers.split("|")

    winning_numbers = to_integer(winning_numbers)
    my_numbers = to_integer(my_numbers)

    matching_numbers_amount = 0

    for my_number in my_numbers:
        if my_number in winning_numbers:
            matching_numbers_amount += 1

    current_card_amount = _instances[i]

    for next_card in range(matching_numbers_amount):
        _instances[i + next_card + 1] += current_card_amount

print(sum(_instances))

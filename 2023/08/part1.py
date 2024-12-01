#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

# network
T = {}

# get the instructions series
instructions = lines.pop(0)

for line in lines:
    # get the values
    value, next_values = line.split("=")
    value = value.strip()

    l, r = next_values.strip()[1:-1].split(",")
    r = r.strip()

    # build the network
    T[value] = (l, r)

node, count, ii = "AAA", 0, 0

# finding Z
while node != "ZZZ":
    if ii >= len(instructions):
        ii = 0

    instruction = instructions[ii]

    l, r = T[node]

    match instruction:
        case "L":
            node = l
        case "R":
            node = r

    count += 1
    ii += 1

print(count)

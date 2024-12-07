#!/usr/bin/env pypy

import os
from operator import add, mul
from itertools import product

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))


def compute(total, operands, operators):
    cmp = operands[0]

    for operand, operator in zip(operands[1:], operators):
        cmp = operator(cmp, operand)

        if cmp > total:
            return False

    return cmp == total


out = 0
for line in lines:
    total, right = line.split(": ")

    total = int(total)
    operands = map(int, right.split())

    p = product([mul, add], repeat=len(operands))
    for operators in p:
        result = compute(total, operands, operators)

        if result is True:
            out += total
            break

print(out)

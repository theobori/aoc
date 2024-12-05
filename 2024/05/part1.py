#!/usr/bin/env pypy

import os


with os.fdopen(0) as f:
    blocks = list(filter(lambda x: len(x) > 0, f.read().split("\n\n")))

orders, produces = blocks

nexts = {}

orders = orders.splitlines()
for order in orders:
    left, right = map(int, order.split("|"))

    if not left in nexts:
        nexts[left] = [right]
    else:
        nexts[left].append(right)

produces = produces.splitlines()
produces = map(lambda p: map(int, p.split(",")), produces)


def is_correct(produce, nexts):
    for i in range(len(produce) - 1):
        head, others = produce[i], produce[i + 1 :]

        if not head in nexts:
            return False

        allowed_nexts = nexts[head]

        for rule in others:
            if not rule in allowed_nexts:
                return False

    return True


out = 0
for produce in produces:
    if is_correct(produce, nexts) is True:
        out += produce[len(produce) // 2]

print(out)

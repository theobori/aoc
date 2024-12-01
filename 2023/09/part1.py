#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

_sum = 0

for line in lines:
    history = [list(map(int, line.split(" ")))]
    h_idx = 0

    while True:
        next_line, idx = [], 0

        while idx + 1 < len(history[h_idx]):
            d = history[h_idx][idx + 1] - history[h_idx][idx]

            next_line.append(d)
            idx += 1

        history.append(next_line)
        h_idx += 1

        if all(x == 0 for x in next_line):
            break

    _sum += sum(h[-1] for h in history)

print(_sum)

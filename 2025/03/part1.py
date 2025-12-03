#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    banks = f.read().strip().splitlines()

n = len(banks[0])
ans = 0

for bank in banks:
    best = float("-inf")
    q = deque(enumerate(bank))
    while q:
        i, s = q.popleft()

        if len(s) == 2:
            best = max(best, int("".join(s)))
            continue

        for next_i in range(i + 1, n):
            q.append((next_i, s + bank[next_i]))

    ans += best

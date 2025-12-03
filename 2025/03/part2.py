#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    banks = f.read().strip().splitlines()

n = len(banks[0])
ans = 0

for bank in banks:
    st = deque()

    for i, j in enumerate(bank):
        while st and st[-1] < j and n - i + len(st) > 12:
            st.pop()

        if len(st) < 12:
            st.append(j)

    ans += int("".join(st))

print(ans)

#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    ranges = f.read().strip().split(",")

ans = 0
for r in ranges:
    start, end = [int(x) for x in r.split("-")]

    for _id in range(start, end + 1):
        _id_str = str(_id)
        n = len(_id_str)
        if n % 2 != 0:
            continue

        half_n = n // 2

        if _id_str[:half_n] == _id_str[half_n:]:
            ans += _id

print(ans)

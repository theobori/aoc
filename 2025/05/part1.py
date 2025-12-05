#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    ranges_str, ids_str = f.read().strip().split("\n\n")

ranges = []
for range_str in ranges_str.splitlines():
    arr = range_str.split("-")
    r = range(int(arr[0]), int(arr[1]) + 1)

    ranges.append(r)

ids = list(map(int, ids_str.splitlines()))

ans = 0
for _id in ids:
    for _range in ranges:
        if _id in _range:
            ans += 1
            break

print(ans)

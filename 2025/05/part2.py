#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    ranges_str, ids_str = f.read().strip().split("\n\n")

ranges = []
for range_str in ranges_str.splitlines():
    pair = list(map(int, range_str.split("-")))

    ranges.append(pair)

ans = 0

n = len(ranges)
ranges = deque(ranges)

for _ in range(n):
    start, end = ranges.popleft()

    for i, (other_start, other_end) in enumerate(ranges):
        if other_start <= start <= other_end and end >= other_end:
            ranges[i][1] = end
            break
        if other_start <= end <= other_end and start <= other_start:
            ranges[i][0] = start
            break
        if other_start <= start <= end <= other_end:
            break
        if start <= other_start and end >= other_end:
            ranges[i][0] = start
            ranges[i][1] = end
            break
    else:
        ranges.append([start, end])

ans = 0
for start, end in ranges:
    ans += end - start + 1

print(ans)

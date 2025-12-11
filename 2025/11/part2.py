#!/usr/bin/env python

import os

from collections import defaultdict
from functools import cache

with os.fdopen(0) as f:
    lines = [line.split(": ") for line in f.read().splitlines() if len(line) > 0]

graph = defaultdict(list)
for _input, outputs in lines:
    for output in outputs.split():
        graph[_input].append(output)


@cache
def dfs(device, final):
    if device == final:
        return 1

    out = 0
    for neighbor in graph[device]:
        out += dfs(neighbor, final)

    return out


ans = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out") + dfs(
    "svr", "fft"
) * dfs("fft", "dac") * dfs("dac", "out")

print(ans)

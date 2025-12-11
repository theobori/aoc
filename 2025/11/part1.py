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
def dfs(device):
    if device == "out":
        return 1

    out = 0
    for neighbor in graph[device]:
        out += dfs(neighbor)

    return out


ans = dfs("you")

print(ans)

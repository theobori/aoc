#!/usr/bin/env pypy

import os

from collections import deque

with os.fdopen(0) as f:
    lines = filter(lambda x: len(x) > 0, f.read().splitlines())

w, h = 101, 103

robots = []
for line in lines:
    p, v = map(
        lambda el: map(int, el.split(",")),
        line.replace("p=", "").replace("v=", "").split(),
    )

    robots.append([p, v])

for step in range(1, 10**9):
    visited = set()
    for i in range(len(robots)):
        robots[i][0][0] = (robots[i][0][0] + robots[i][1][0]) % w
        robots[i][0][1] = (robots[i][0][1] + robots[i][1][1]) % h
        visited.add((robots[i][0][0], robots[i][0][1]))

    if len(visited) == len(robots):
        print(step)
        break

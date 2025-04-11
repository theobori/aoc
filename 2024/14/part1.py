#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = filter(lambda x: len(x) > 0, f.read().splitlines())

w, h = 101, 103

quadrants = (
    (0, 0, w // 2 - 1, h // 2 - 1),
    (w // 2 + 1, 0, w, h // 2 - 1),
    (0, h // 2 + 1, w // 2 - 1, h),
    (w // 2 + 1, h // 2 + 1, w, h),
)

robots = []
for line in lines:
    p, v = map(
        lambda el: map(int, el.split(",")),
        line.replace("p=", "").replace("v=", "").split(),
    )

    robots.append([p, v])

for _ in range(100):
    for i in range(len(robots)):
        robots[i][0][0] = (robots[i][0][0] + robots[i][1][0]) % w
        robots[i][0][1] = (robots[i][0][1] + robots[i][1][1]) % h


q = [0] * len(quadrants)
for i, (qx, qy, qw, qh) in enumerate(quadrants):
    for robot in robots:
        rx, ry = robot[0]

        if rx >= qx and rx <= qx + qw and ry >= qy and ry <= qy + qh:
            q[i] += 1

total = 1
for n in q:
    total *= n

print(total)

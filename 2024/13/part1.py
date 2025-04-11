#!/usr/bin/env python

import os
import numpy as np

with os.fdopen(0) as f:
    machines = list(
        map(
            lambda m: m.splitlines(),
            filter(lambda x: len(x) > 0, f.read().split("\n\n")),
        )
    )

tokens = 0
for i, (a, b, p) in enumerate(machines):
    ax, ay = list(map(int, a.replace("Button A: X+", "").replace(" Y+", "").split(",")))
    bx, by = list(map(int, b.replace("Button B: X+", "").replace(" Y+", "").split(",")))
    px, py = list(map(int, p.replace("Prize: X=", "").replace(" Y=", "").split(",")))

    a, b = np.linalg.solve(np.array([[ax, bx], [ay, by]]), [px, py]).round().astype(int)

    x = a * ax + b * bx
    y = a * ay + b * by
    if (x, y) != (px, py) or a > 100 or b > 100:
        continue

    tokens += 3 * a + b

print(tokens)

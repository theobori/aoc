#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

lines = map(lambda s: map(int, s.split()), lines)
left, right = zip(*lines)

print(sum(map(lambda s: s * right.count(s), left)))

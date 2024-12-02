#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = list(filter(lambda x: len(x) > 0, f.read().splitlines()))

lines = map(lambda s: map(int, s.split()), lines)


def is_safe(levels):
    is_same_direction = (
        sorted(levels) == levels or sorted(levels, reverse=True) == levels
    )

    is_diffs_allowed = all(
        map(
            lambda x: 1 <= x <= 3,
            [abs(levels[i + 1] - levels[i]) for i in range(len(levels) - 1)],
        )
    )

    return is_same_direction and is_diffs_allowed


print(len(filter(is_safe, lines)))

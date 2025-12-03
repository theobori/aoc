#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    ranges = f.read().strip().split(",")


def is_invalid(_id_str, n):
    half_n = n // 2

    for group_len in range(half_n, 0, -1):
        group_ref = _id_str[:group_len]

        for i in range(group_len, n, group_len):
            group = _id_str[i : i + group_len]

            if group != group_ref:
                break
        else:
            return True

    return False


ans = 0
for r in ranges:
    start, end = [int(x) for x in r.split("-")]

    for _id in range(start, end + 1):
        _id_str = str(_id)
        n = len(_id_str)

        if is_invalid(_id_str, n):
            ans += _id

print(ans)

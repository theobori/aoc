#!/usr/bin/env pypy

import os
import re

with os.fdopen(0) as f:
    content = f.read()


def do_mul_str(s):
    left, right = map(int, s[4:-1].split(","))
    return left * right


muls = re.findall("mul\(\d{1,3},\d{1,3}\)", content)
print(sum(map(do_mul_str, muls)))

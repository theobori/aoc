#!/usr/bin/env pypy

import os
import re

with os.fdopen(0) as f:
    content = f.read()


def do_mul_str(s):
    left, right = map(int, s[4:-1].split(","))
    return left * right


out, flag = 0, True
ops = re.findall("(mul\(\d{1,3},\d{1,3}\))|(don't\(\))|(do\(\))", content)

while ops:
    (op,) = filter(lambda s: len(s) > 0, ops.pop(0))

    if op == "do()":
        flag = True
    elif op == "don't()":
        flag = False
    elif op.startswith("mul"):
        if flag is True:
            out += do_mul_str(op)
    else:
        raise Exception("Unknown operation")


print(out)

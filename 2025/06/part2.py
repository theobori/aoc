#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [line for line in f.read().splitlines() if len(line) > 0]

operators = list(lines.pop())

m = len(operators)

ans = i = 0
while i < m:
    operator = operators[i]

    operators[i] = ""

    result = 1 if operator == "*" else 0

    while i < m and operators[i] != "*" and operators[i] != "+":
        curr = ""

        for line in lines:
            if line[i].isdigit():
                curr += line[i]

        if curr.isdigit():
            curr = int(curr)

            if operator == "*":
                result *= curr
            elif operator == "+":
                result += curr
            else:
                raise Exception("Unknown operator")

        i += 1

    ans += result

print(ans)

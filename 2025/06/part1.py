#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    lines = [
        [el for el in line.split() if len(el) > 0]
        for line in f.read().splitlines()
        if len(line) > 0
    ]

operators = lines.pop()
m = len(operators)

results = [1 if operator == "*" else 0 for operator in operators]

for line in lines:
    for i in range(m):
        number = int(line[i])

        if operators[i] == "*":
            results[i] *= number
        elif operators[i] == "+":
            results[i] += number
        else:
            raise Exception("Unknown operator")

ans = sum(results)

print(ans)

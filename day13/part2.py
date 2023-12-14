#!/usr/bin/env pypy

with open(0) as f:
    patterns = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n\n")
        )
    )

_sum = 0

def get_reflection(pattern):
    for i in range(1, len(pattern)):
        a = pattern[:i]
        b = pattern[i:]

        a = a[::-1][:len(b)]
        b = b[:len(a)]

        c = 0

        for line_a, line_b in zip(a, b):
            for char_a, char_b in zip(line_a, line_b):
                if char_a != char_b:
                    c += 1

        if c == 1:
            return i
    
    return 0

for lines in patterns:
    lines = lines.splitlines()

    line = get_reflection(lines)

    rows = [[line[x] for line in lines] for x in range(len(lines[0]))]
    row = get_reflection(rows)

    _sum += line * 100 + row

print(_sum)

#!/usr/bin/env pypy

SPELLED_DIGITS = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
)

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

_sum = 0

for line in lines:
    first = -1
    last = -1

    for i, char in enumerate(line):
        if first != -1 and last != -1:
            break

        # check for digit
        if char.isdigit() == True:
            if first == -1:
                first = char
            else:
                last = char
            
            continue
        
        # check for a spelled digit
        for j, spelled_digit in enumerate(SPELLED_DIGITS):
            if line[i:i + len(spelled_digit)] == spelled_digit:
                value = str(j + 1)

                if first == -1:
                    first = value
                else:
                    last = value
        
    if last == -1:
        _sum += int(first + first)
    else:
        _sum += int(first + last)

print(_sum)

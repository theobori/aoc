#!/usr/bin/env python

with open("../input.txt") as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

numbers = []

checks = (
    (-1, 0), (-1, -1), (0, -1), (-1, 1),
    (1, 0), (1, 1), (0, 1), (1, -1)
)

for y, line in enumerate(lines):
    x = 0

    while x < len(line):        
        size = 0
        is_valid_number = False
        number_x = x
        
        while number_x < len(line) and line[number_x].isdigit():
            for (check_y, check_x) in checks:
                try:
                    char = lines[y + check_y][number_x + check_x]
                    
                    if not char.isdigit() and char != ".":
                        is_valid_number = True
                        break
                except:
                    continue

            size += 1
            number_x += 1
        
        if is_valid_number == True:
            numbers.append(int(lines[y][number_x - size:number_x]))
            x += size

            continue    
        
        x += 1

print(sum(numbers))

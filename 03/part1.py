#!/usr/bin/env pypy

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

height, width = len(lines), len(lines[0])

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
            for (dy, dx) in checks:
                ny, nx = y + dy, number_x + dx
                
                if ny < 0 or ny >= height:
                    continue
                
                if nx < 0 or nx >= width:
                    continue
                
                char = lines[ny][nx]
                
                if not char.isdigit() and char != ".":
                    is_valid_number = True
                    break

            size += 1
            number_x += 1
        
        if is_valid_number == True:
            numbers.append(int(lines[y][number_x - size:number_x]))
            x += size

            continue    
        
        x += 1

print(sum(numbers))

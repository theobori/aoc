#!/usr/bin/env pypy

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

lines = list(map(list, lines))
height, width = len(lines), len(lines[0])

def get_rocks(lines):
    return [(y, x) for y, line in enumerate(lines) for x in range(len(line)) if line[x] == "O"]

ref_rocks = get_rocks(lines)

CYCLE_LIMIT = 1000
cycle = 1

for i in range(1_000_000_000):
    for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        # update the rocks
        if (dy, dx) in ((-1, 0), (0, -1)):
            rocks = get_rocks(lines)
        else:
            rocks = get_rocks(lines)[::-1]
        
        for y, x in rocks:
            ry, rx = y, x

            while rx + dx >= 0 and \
                ry + dy >= 0 and \
                rx + dx < width and \
                ry + dy < height and \
                lines[ry + dy][rx + dx] == ".":
                    
                ry += dy
                rx += dx
            
            lines[y][x] = "."
            lines[ry][rx] = "O"
    
    rocks = get_rocks(lines)
    
    if rocks == ref_rocks:
        break
        
    if cycle >= CYCLE_LIMIT:
        cycle = 0
        ref_rocks = rocks
    cycle += 1

print(sum(height - y for y, _ in get_rocks(lines)))

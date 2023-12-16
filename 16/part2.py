#!/usr/bin/env pypy

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

height, width = len(lines), len(lines[0])

M = {
    "|": {
        (0, 1): ((1, 0), (-1, 0)),
        (0, -1): ((1, 0), (-1, 0)),
    },
    "-": {
        (1, 0): ((0, 1), (0, -1)),
        (-1, 0): ((0, 1), (0, -1)),
    },
    "/": {
        (0, 1): ((-1, 0),),
        (0, -1): ((1, 0),),
        (1, 0): ((0, -1),),
        (-1, 0): ((0, 1),)
    },
    "\\": {
        (0, 1): ((1, 0),),
        (0, -1): ((-1, 0),),
        (1, 0): ((0, 1),),
        (-1, 0): ((0, -1),),
    },
    ".": {},
}

def s(pos, dir):
    Q, V = [(pos, dir)], [(pos, dir)]

    while Q:
        p, d = Q.pop(0)
        
        y, x = p
        
        dirs = M[lines[y][x]]
        
        if not d in dirs.keys():
            dirs = (d,)
        else:
            dirs = dirs[d]
        
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            
            if ny < 0 or ny >= height:
                continue
            
            if nx < 0 or nx >= width:
                continue
            
            v = ((ny, nx), (dy ,dx))
            
            if not v in V:
                Q.append(v)                
                V.append(v)                
            
    return len(set([(*p,) for (p, _) in V]))

p, best = [], 0

for x in range(width):
    p.append(((0, x), (1, 0)))
    p.append(((height - 1, x), (-1, 0)))

for y in range(height):
    p.append(((y, 0), (0, 1)))
    p.append(((y, width - 1), (0, -1)))
    
for pos, dir in p:
    tiles = s(pos, dir)
    
    if tiles > best:
        best = tiles

print(best)

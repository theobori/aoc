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

Q, V = [((0, 0), (0, 1))], [((0, 0), (0, 1))]

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
        
print(len(set([(*p,) for (p, _) in V])))

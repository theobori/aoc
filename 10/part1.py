#!/usr/bin/env pypy

with open(0) as f:
    M = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

SYMBOLS = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
    "S": ((-1, 0), (1, 0), (0, -1), (0, 1))
}

ADJ_SYMBOLS = {
    (-1, 0): "F|7",
    (1, 0): "L|J",
    (0, -1): "F-L",
    (0, 1): "7-J",
}

S = (None, None)

for y, line in enumerate(M):
    if S != (None, None):
        break

    for x, c in enumerate(line):
        if c == "S":
            S = (y, x)
            break

def get_neighbors(matrice, coord):
    neighbors = []
    
    y, x = coord
    symbol = matrice[y][x]
    
    if not symbol in SYMBOLS.keys():
        return neighbors
    
    deltas = SYMBOLS[symbol]
    
    for dy, dx in deltas:
        ny, nx = y + dy, x + dx
    
        if ny < 0 or ny >= len(matrice):
            continue
        
        if nx < 0 or nx >= len(matrice[ny]):
            continue
        
        if not matrice[ny][nx] in ADJ_SYMBOLS[(dy, dx)]:
            continue

        neighbors.append((ny, nx))
    
    return neighbors
    
Q, V, step_max = [(S, 0)], [S], -1

while Q:
    coord, step = Q.pop(0)
    y, x = coord
    
    if M[y][x] == ".":
        continue
    
    if step > step_max:
        step_max = step

    neighbors = get_neighbors(M, coord)

    for neighbor in neighbors:
        if not neighbor in V:
            Q.append((neighbor, step + 1))
            V.append(neighbor)

print(step_max)

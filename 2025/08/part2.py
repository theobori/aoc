#!/usr/bin/env pypy

import os
import math

from collections import deque, defaultdict

with os.fdopen(0) as f:
    positions = [
        tuple(map(int, line.split(",")))
        for line in f.read().splitlines()
        if len(line) > 0
    ]


def get_euclidean_distance_3d(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)


n = len(positions)

triplets = []
for i in range(n):
    p = positions[i]

    for j in range(i + 1, n):
        q = positions[j]
        d = get_euclidean_distance_3d(p, q)
        triplets.append((d, i, j))

triplets.sort(key=lambda t: t[0])

graph = defaultdict(set)


def are_all_connected(graph, i):
    seen = {i}
    q = deque([i])

    size = 0
    while q:
        node = q.popleft()

        size += 1

        for neighbor in graph[node]:
            if not neighbor in seen:
                q.append(neighbor)
                seen.add(neighbor)

    return size == n


ans = 0
for _, i, j in triplets:
    graph[i].add(j)
    graph[j].add(i)

    if are_all_connected(graph, i):
        ans = positions[i][0] * positions[j][0]
        break

print(ans)

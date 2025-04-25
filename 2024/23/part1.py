#!/usr/bin/env pypy

import os

from collections import defaultdict

with os.fdopen(0) as f:
    connections = map(
        lambda el: el.split("-"), filter(lambda x: len(x) > 0, f.read().splitlines())
    )

computers_graph = defaultdict(set)
for computer_a, computer_b in connections:
    computers_graph[computer_a].add(computer_b)
    computers_graph[computer_b].add(computer_a)

cliques = set()


# Bron-Kerbosch Algorithm
# r -> current clique
# p -> candidate set
# x -> exclusion set
def bk(r, p, x):
    if len(r) == 3:
        cliques.add(tuple(sorted(r)))
        return

    for v in p:
        neighbors = computers_graph[v]
        bk(r.union({v}), p.intersection(neighbors), x.intersection(neighbors))
        x = x.union({v})
        p = p - {v}


p = set(computers_graph.keys())

bk(set(), p, set())

total = len(filter(lambda path: any(c[0] == "t" for c in path), cliques))
print(total)

#!/usr/bin/env pypy

from math import lcm

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

# network
T = {}
# nodes ending with A
A = []

# get the instructions series
instructions = lines.pop(0)

for line in lines:
    # get the values
    value, next_values = line.split("=")
    value = value.strip()
    
    l, r = next_values.strip()[1:-1].split(",")
    r = r.strip()
    
    # build the network
    T[value] = (l, r)
    
    # keeping nodes starting with A
    if value.endswith("A"):
        A.append(value)
    
counts = []
# instruction index
ii = 0

# compute the steps for each nodes
for ni in range(len(A)):
    count = 0
    
    while not A[ni].endswith("Z"):
        if ii >= len(instructions):
            ii = 0
        
        instruction = instructions[ii]
    
        l, r = T[A[ni]]

        match instruction:
            case "L":
                A[ni] = l
            case "R":
                A[ni] = r
            
        count +=1
        ii += 1
    
    counts.append(count)
                            
print(counts, lcm(*counts))

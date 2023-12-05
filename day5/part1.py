#!/usr/bin/env python

with open("input.txt") as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n\n")
        )
    )

seeds = lines.pop(0)
_, seeds_values = seeds.split(": ")

SEEDS = list(map(int, seeds_values.split(" ")))

M = {}

for line in lines:
    line = line.split("\n")

    header = line.pop(0)
    header = header.split(" ")
    header = header.pop(0)

    destination_name, _, source_name = header.split("-")
    
    entries = list(filter(lambda x: len(x) > 0, line))
    
    for entry in entries:
        entry = list(map(int, entry.split(" ")))
    
        destination, source, length = entry
        
        key = (destination_name, source_name)
        
        entry = tuple(entry)
        
        if not key in M.keys():
            M[key] = [entry]
        else:
            M[key] += [entry]
        
lowest_location = -1

for seed in SEEDS:
    _next = seed
    
    for (destination_name, source_name), entries in M.items():
        for destination, source, length in entries:
            if length > 0:
                length -= 1

            if length <= 0:
                continue
            
            if source <= _next <= source + length:
                _next -= source - destination
                break
        
        if source_name == "location":
            if lowest_location == -1 or _next < lowest_location:
                lowest_location = _next
        
print(lowest_location)

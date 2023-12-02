#!/usr/bin/env python

with open("../input.txt") as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

_sum = 0

for line in lines:
    (game_id, game) = line.split(":")

    game_id = int(game_id[5:])
    
    subsets = game.split(";")
    subsets = list(map(lambda subset: subset.split(","), subsets))
    
    few_colors = {}
    
    for subset in subsets:
        subset = map(lambda x: x[1:].split(" "), subset)
        subset = list(subset)
        
        for amount, color in subset:
            amount = int(amount)

            if color in few_colors.keys():
                few_colors[color].append(amount)
            else:
                few_colors[color] = [amount]
    
    power = 1

    for amounts in few_colors.values():
        power *= max(amounts)
    
    _sum += power

print(_sum)

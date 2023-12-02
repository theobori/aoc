#!/usr/bin/env python

MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14 
}

with open("../input.txt") as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

valid_games = []

for line in lines:
    (game_id, game) = line.split(":")

    game_id = int(game_id[5:])
    
    subsets = game.split(";")
    subsets = list(map(lambda subset: subset.split(","), subsets))
    
    is_valid = True
    
    for subset in subsets:
        subset = map(lambda x: x[1:].split(" "), subset)
        subset = list(subset)
        
        for amount, color in subset:
            amount = int(amount)

            if amount > MAX_CUBES[color]:
                is_valid = False
                break
        
        
    if is_valid == True:
        valid_games.append(game_id)

print(sum(valid_games))

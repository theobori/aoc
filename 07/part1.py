#!/usr/bin/env pypy

from typing import Tuple
from functools import cmp_to_key

with open(0) as f:
    lines = list(
        filter(
            lambda x: len(x) > 0,
            f.read().split("\n")
        )
    )

def c(hand: str, *amounts: Tuple[int, int]) -> bool:
    counts = []
    
    while len(hand) > 0:
        value = hand[0]

        counts.append(hand.count(value))
        hand = hand.replace(value, "")
    
    for value, amount in amounts:
        if counts.count(value) != amount:
            return False
    
    return True

SYMBOL_ORDER = (
    "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2",
)

HAND_TYPES = (
    ((1, 5),),
    ((2, 1), (1, 3)),
    ((2, 2),),
    ((3, 1), (1, 2)),
    ((3, 1), (2, 1)),
    ((4, 1),),
    ((5, 1),),
)

order = [[] for _ in range(len(HAND_TYPES))]

def order_cmp(hand_one: Tuple[int], hand_two: Tuple[int]) -> int:
    for symbol_one, symbol_two in zip(hand_one[0], hand_two[0]):
        i_one = SYMBOL_ORDER.index(symbol_one)
        i_two = SYMBOL_ORDER.index(symbol_two)
        
        if i_one > i_two:
            return -1
        
        if i_one < i_two:
            return 1
    
    return 0

for line in lines:
    hand, bid = line.split(" ")
    
    bid = int(bid)
    
    for i, hand_type in enumerate(HAND_TYPES):
        if c(hand, *hand_type) == True:
            order[i].append((hand, bid))

for i in range(len(order)):
    order[i] = sorted(order[i], key=cmp_to_key(order_cmp))

_sum = 0
rank = 1

for hands_type in order:
    for (hand, bid) in hands_type:
        _sum += bid * rank
        rank += 1

print(_sum)
    
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
    "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J",
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

def symbol_cmp(symbol_one: str, symbol_two: str) -> int:
    i_one = SYMBOL_ORDER.index(symbol_one)
    i_two = SYMBOL_ORDER.index(symbol_two)
    
    if i_one > i_two:
        return -1
    
    if i_one < i_two:
        return 1

    return 0

def hand_cmp(hand_one: str, hand_two: str) -> int:
    for symbol_one, symbol_two in zip(hand_one, hand_two):
        cmp = symbol_cmp(symbol_one, symbol_two)
        
        if cmp != 0:
            return cmp
        
    return 0

def get_type(hand: str) -> int:
    for i, hand_type in enumerate(HAND_TYPES):
        if c(hand, *hand_type) == True:
            return i
    
    return 0

def order_cmp(hand_one: Tuple[int], hand_two: Tuple[int]) -> int:
    return hand_cmp(hand_one[0], hand_two[0])

def j_hand(hand: str) -> str:
    for symbol in SYMBOL_ORDER:
        if symbol == "J":
            continue

        new_hand = old_hand.replace("J", symbol)
        
        t_hand = get_type(hand)
        t_new_hand = get_type(new_hand)
        
        if t_new_hand > t_hand:
            hand = new_hand
            continue
    
        if t_new_hand == t_hand:
            if hand_cmp(new_hand, hand) == -1:    
                hand = new_hand
    
    return hand

for line in lines:
    hand, bid = line.split(" ")
    
    bid = int(bid)
    old_hand = hand
    
    if "J" in hand:
        hand = j_hand(hand)

    order[get_type(hand)].append((old_hand, bid))

for i in range(len(order)):
    order[i] = sorted(order[i], key=cmp_to_key(order_cmp))

_sum = 0
rank = 1

for hands_type in order:
    for (hand, bid) in hands_type:
        _sum += bid * rank
        rank += 1

print(_sum)

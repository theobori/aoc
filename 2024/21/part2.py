#!/usr/bin/env pypy

import os

try:
    from functools import cache as memoize
except ImportError:
    # Better to use cache from functools if available
    # Not the case for pypy <= 3
    def memoize(func):
        cache = {}

        def memoized_func(*args):
            if args in cache:
                return cache[args]
            result = func(*args)
            cache[args] = result
            return result

        return memoized_func


with os.fdopen(0) as f:
    codes = filter(lambda x: len(x) > 0, f.read().splitlines())

NUMERIC_KEYPAD = {
    "7": (0, 3),
    "8": (1, 3),
    "9": (2, 3),
    "4": (0, 2),
    "5": (1, 2),
    "6": (2, 2),
    "1": (0, 1),
    "2": (1, 1),
    "3": (2, 1),
    "": (0, 0),
    "0": (1, 0),
    "A": (2, 0),
}

DIRECTION_KEYPAD = {
    "": (0, 1),
    "^": (1, 1),
    "A": (2, 1),
    "<": (0, 0),
    "v": (1, 0),
    ">": (2, 0),
}


def get_keypad(keypad_id):
    return NUMERIC_KEYPAD if keypad_id == 0 else DIRECTION_KEYPAD


def keys_moves(keypad_id, from_symbol, to_symbol):
    keypad = get_keypad(keypad_id)
    fx, fy = keypad[from_symbol]
    tx, ty = keypad[to_symbol]

    dh = tx - fx
    dv = ty - fy

    h = ("<" if dh < 0 else ">") * abs(dh)
    v = ("^" if dv > 0 else "v") * abs(dv)

    # Predecence
    if keypad_id == 0:
        if fy == 0 and tx == 0:
            return v + h + "A"
        if fx == 0 and ty == 0:
            return h + v + "A"
        if dh < 0:
            return h + v + "A"
        if dh >= 0:
            return v + h + "A"
    else:
        if fx == 0 and ty == 1:
            return h + v + "A"
        if fy == 1 and tx == 0:
            return v + h + "A"
        if dh < 0:
            return h + v + "A"
        if dh >= 0:
            return v + h + "A"


def keys_sequence(keypad_id, sequence):
    output = ""

    from_symbol = "A"
    for to_symbol in sequence:
        keys = keys_moves(keypad_id, from_symbol, to_symbol)
        output += keys

        from_symbol = to_symbol

    return output


@memoize
def keys_count(key_seq, depth):
    if depth == 0:
        return len(key_seq)

    from_symbol = "A"
    count = 0

    for to_symbol in key_seq:
        moves = keys_moves(1, from_symbol, to_symbol)
        count += keys_count(moves, depth - 1)
        from_symbol = to_symbol

    return count


total = 0
for code in codes:
    # With numeric keypad
    keys = keys_sequence(0, code)

    # With the 25 directional keypads
    count = keys_count(keys, 25)
    total += int(code[:-1]) * count


print(total)

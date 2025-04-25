#!/usr/bin/env pypy

import os

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
        if fy == 1 and tx == 0:
            return v + h + "A"
        if fx == 0 and tx == 1:
            return h + v + "A"
        if dh < 0:
            return h + v + "A"
        if dh >= 0:
            return v + h + "A"


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


total = 0
for code in codes:
    keys = keys_sequence(0, code)
    keys = keys_sequence(1, keys)
    keys = keys_sequence(1, keys)

    total += int(code[:-1]) * len(keys)


print(total)

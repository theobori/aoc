#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    registers, program = filter(lambda x: len(x) > 0, f.read().split("\n\n"))


a, b, c = [int(r[r.index(":") + 2 :]) for r in registers.splitlines()]
program = map(int, program.replace("\n", "").replace("Program: ", "").split(","))


def combo_operand(value):
    if 0 <= value <= 3:
        return value

    if value == 4:
        return a
    if value == 5:
        return b
    if value == 6:
        return c

    raise Exception("invalid value for combo operand")


def literal_operand(value):
    return value


def dv(operand):
    numerator = a
    denominator = 2 ** combo_operand(operand)

    return int(numerator / denominator)


out = []
ip = 0
while ip < len(program):
    opcode = program[ip]
    ip += 1
    operand = program[ip]

    if opcode == 0:
        a = dv(operand)
    elif opcode == 1:
        b ^= literal_operand(operand)
    elif opcode == 2:
        b = (combo_operand(operand) % 8) & 0b111
    elif opcode == 3:
        if a != 0:
            ip = literal_operand(operand)
            continue
    elif opcode == 4:
        b ^= c
    elif opcode == 5:
        out.append(combo_operand(operand) % 8)
    elif opcode == 6:
        b = dv(operand)
    elif opcode == 7:
        c = dv(operand)
    else:
        raise Exception("unknown opcode")

    ip += 1

print(",".join(map(str, out)))

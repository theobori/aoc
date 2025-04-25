#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    _output_bits, _connection_gates = filter(
        lambda x: len(x) > 0, f.read().split("\n\n")
    )

outputs_bits = {}
for line in _output_bits.splitlines():
    wire_name, output_bit = line.split(": ")
    outputs_bits[wire_name] = int(output_bit)

connection_gates = {}
for line in _connection_gates.splitlines():
    gate_op, destination = line.split(" -> ")

    connection_gates[destination] = tuple(gate_op.split())

# x, y = 0, 0
# for wire in sorted(outputs_bits.keys(), reverse=True):
#     if wire.startswith("x"):
#         x = (x << 1) | outputs_bits[wire]
#     elif wire.startswith("y"):
#         y = (y << 1) | outputs_bits[wire]

# z = x + y
# z_len = len(bin(z)[2:])

# See https://www.reddit.com/r/adventofcode/comments/1hla5ql/2024_day_24_part_2_a_guide_on_the_idea_behind_the/

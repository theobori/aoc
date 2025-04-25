#!/usr/bin/env pypy

import os
import operator


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

OPS = {
    "XOR": operator.xor,
    "OR": operator.or_,
    "AND": operator.and_,
}


def compute_gate(gate):
    if gate in outputs_bits:
        return outputs_bits[gate]

    left, op, right = connection_gates[gate]

    outputs_bits[gate] = OPS[op](compute_gate(left), compute_gate(right))

    return outputs_bits[gate]


zs = sorted(
    filter(lambda name: name.startswith("z"), connection_gates.keys()), reverse=True
)

z_output = "".join(str(compute_gate(z)) for z in zs)
decimal_output = int(
    z_output,
    2,
)

print(decimal_output)

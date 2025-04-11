#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    registers, program = filter(lambda x: len(x) > 0, f.read().split("\n\n"))


a, b, c = [int(r[r.index(":") + 2 :]) for r in registers.splitlines()]
program = map(int, program.replace("\n", "").replace("Program: ", "").split(","))


class Computer:
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.ip = 0

    def combo_operand(self, value):
        if 0 <= value <= 3:
            return value

        if value == 4:
            return self.a
        if value == 5:
            return self.b
        if value == 6:
            return self.c

        raise Exception("invalid value for combo operand")

    def literal_operand(self, value):
        return value

    def dv(self, operand):
        numerator = self.a
        denominator = 2 ** self.combo_operand(operand)

        return int(numerator / denominator)

    def run(self):
        out = []
        while self.ip < len(self.program):
            opcode = program[self.ip]
            self.ip += 1
            operand = program[self.ip]

            if opcode == 0:
                self.a = self.dv(operand)
            elif opcode == 1:
                self.b ^= self.literal_operand(operand)
            elif opcode == 2:
                self.b = (self.combo_operand(operand) % 8) & 0b111
            elif opcode == 3:
                if self.a != 0:
                    self.ip = self.literal_operand(operand)
                    continue
            elif opcode == 4:
                self.b ^= self.c
            elif opcode == 5:
                out.append(self.combo_operand(operand) % 8)
            elif opcode == 6:
                self.b = self.dv(operand)
            elif opcode == 7:
                self.c = self.dv(operand)
            else:
                raise Exception("unknown opcode")

            self.ip += 1

        return out

    def reset(self, a, b, c):
        self.ip = 0
        self.a = a
        self.b = b
        self.c = c


computer = Computer(0, b, c, program)

i = 1
out = []
while True:
    if out == program:
        print(i)
        break

    computer.reset(i, b, c)
    out = computer.run()

    if len(out) < len(program):
        i *= 2
        continue

    for j in range(len(out) - 1, -1, -1):
        if out[j] != program[j]:
            i += 8**j
            break

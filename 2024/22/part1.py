#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    initial_secret_numbers = filter(lambda x: len(x) > 0, f.read().splitlines())


def mix(secret_number, value):
    return secret_number ^ value


def prune(secret_number):
    return secret_number % 16777216


def next_secret_number(secret_number):
    # Multiply by 64
    result_multiply = secret_number * 64
    # Mix
    secret_number = mix(secret_number, result_multiply)
    # Prune
    secret_number = prune(secret_number)

    # Dividing
    result_divide = int(secret_number / 32)
    # Mix
    secret_number = mix(secret_number, result_divide)
    # Prune
    secret_number = prune(secret_number)

    # Multiply
    result_multiply = secret_number * 2048
    # Mix
    secret_number = mix(secret_number, result_multiply)
    # Prune
    secret_number = prune(secret_number)

    return secret_number


def next_n_secret_number(initial_secret_number, n):
    secret_number = initial_secret_number

    for i in range(n):
        secret_number = next_secret_number(secret_number)

    return secret_number


total = 0
for initial_secret_number in initial_secret_numbers:
    _next = next_n_secret_number(int(initial_secret_number), 2000)
    total += _next

print(total)

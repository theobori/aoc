#!/usr/bin/env pypy

import os

from collections import deque, defaultdict

with os.fdopen(0) as f:
    initial_secret_numbers = map(
        int, filter(lambda x: len(x) > 0, f.read().splitlines())
    )


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


# Quick solution
# This function should take a dict containing every single sequence as key and the total as value
def get_sequences_dict(sequences, initial_secret_number, n):
    secret_number = initial_secret_number
    last_digit = secret_number % 10
    current_sequence = deque()

    sequences_seen = set()

    # Fill the current sequence with the 3 first digits
    for i in range(3):
        tmp_secret_number = next_secret_number(secret_number)
        tmp_last_digit = tmp_secret_number % 10
        current_sequence.append(tmp_last_digit - last_digit)

        secret_number = tmp_secret_number
        last_digit = tmp_last_digit

    for i in range(n - 3):
        tmp_secret_number = next_secret_number(secret_number)
        tmp_last_digit = tmp_secret_number % 10
        current_sequence.append(tmp_last_digit - last_digit)

        # Get the last digit
        last_digit = secret_number % 10
        # Add the sequence the sequences dict with the last digit as value
        key = tuple(current_sequence)

        if not key in sequences_seen:
            sequences[key] += tmp_last_digit
            sequences_seen.add(key)

        # Shift the deque
        current_sequence.popleft()

        secret_number = tmp_secret_number
        last_digit = tmp_last_digit


sequences = defaultdict(int)
for initial_secret_number in initial_secret_numbers:
    get_sequences_dict(sequences, initial_secret_number, 2000)

print(max(sequences.values()))

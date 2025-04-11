#!/usr/bin/env pypy

import os

with os.fdopen(0) as f:
    line = f.read().strip()

blocks = []

is_file = True
_id = 0
for symbol in line:
    number = int(symbol)

    if is_file is True:
        blocks.extend([_id] * number)
        _id += 1
    else:
        blocks.extend([None] * number)

    is_file ^= True

# Quick solution
for i in range(_id - 1, -1, -1):
    # Get the first occurence index
    file_index = blocks.index(i)
    file_size = 0
    # Get the file size

    tmp_file_index = file_index
    while tmp_file_index < len(blocks) and blocks[tmp_file_index] == i:
        file_size += 1
        tmp_file_index += 1

    # Check from the left if it can fits somewhere
    # until it reaches itself
    for j in range(file_index):
        # Check size
        free_space_index = j
        tmp_free_space_index = free_space_index
        while (
            blocks[tmp_free_space_index] is None and tmp_free_space_index < file_index
        ):
            tmp_free_space_index += 1

        free_space_size = tmp_free_space_index - j
        if free_space_size >= file_size:
            # Write on the free space
            for ii in range(free_space_index, free_space_index + file_size):
                blocks[ii] = i
            # Erase the old file location
            for ii in range(file_index, file_index + file_size):
                blocks[ii] = None

            break

total = 0
for i in range(len(blocks)):
    if blocks[i] is None:
        continue

    total += i * blocks[i]

print(total)

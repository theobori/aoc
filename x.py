#!/usr/bin/env python

"""This is a small pure Python executable script designed to
execute AoC Python executable scripts solutions and
to create Nix derivations. It supports multiple Python runtime
if specified as shebang.

It assumes the following file structures.
<year>/<two_digits_problem_id>/part1.py|part2.py
"""

import logging
import subprocess

from subprocess import CompletedProcess, CalledProcessError
from pathlib import Path
from sys import argv, exit, stderr

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

year: int
problem_id: int
part_id: int
try:
    year = int(argv[1])
    problem_id = int(argv[2])
    part_id = int(argv[3])

    assert 0 <= problem_id <= 25
    assert part_id == 1 or part_id == 2
except Exception as e:
    logger.error("An error occured with the CLI arguments.", exc_info=True)
    exit(1)

path_prefix = Path("./", str(year), f"{problem_id:02}")
path_solution = path_prefix / f"part{part_id}.py"

if path_solution.exists() is False:
    logger.error(
        f"The problem {problem_id} of the year {year} has no solution for the part {part_id}."
    )
    exit(1)

subprocess_args = argv[4:]
subprocess_args_str = " ".join(subprocess_args)

completed_process: CompletedProcess[bytes]
try:
    completed_process = subprocess.run(
        f"{path_solution.absolute()} {subprocess_args_str}",
        shell=True,
        check=True,
        capture_output=True,
    )
except CalledProcessError as e:
    print(e.stderr.decode(), file=stderr, end="")
    exit(1)
except Exception:
    exit(1)

print(completed_process.stdout.decode(), end="")

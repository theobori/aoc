#!/usr/bin/env python

"""This is a small pure Python executable script designed to
execute AoC Python executable scripts solutions and
to create Nix derivations. It supports multiple Python runtime
if specified as shebang.

It assumes the following file structures.
<year>/<two_digits_problem_id>/part1.py|part2.py

It is also used to generate my AoC solves statistics.
"""


from subprocess import CalledProcessError
from sys import argv, exit
from typing import NoReturn
from pathlib import Path

from x.runner import runner_run
from x.aoc import AOCSolutionMetadata, aoc_get_solution_filepath
from x.statistics import statistics_create_readme_files

from loguru import logger


def x_run(directory_path: Path) -> NoReturn:
    """Run the Advent Of Code solution.

    Returns:
        NoReturn: No return.
    """

    if len(argv) < 5:
        logger.error("Missing arguments <year> <day> <part>")
        exit(1)

    aoc_solution_metadata: AOCSolutionMetadata
    try:
        aoc_solution_metadata = AOCSolutionMetadata(
            year=int(argv[2]),
            day=int(argv[3]),
            part=int(argv[4]),
        )
    except Exception as e:
        logger.error(e)
        exit(1)

    solution_filepath = aoc_get_solution_filepath(directory_path, aoc_solution_metadata)

    if solution_filepath.exists() is False:
        logger.error(
            f"The problem {aoc_solution_metadata.day} "
            f"of the year {aoc_solution_metadata.year} "
            f"has no solution for the part {aoc_solution_metadata.part}"
        )
        exit(1)

    solution_args = argv[5:]

    run_output: str
    try:
        run_output = runner_run(solution_filepath, solution_args)
    except CalledProcessError as e:
        logger.error(e.stderr.decode())
        exit(1)
    except Exception:
        exit(1)

    print(run_output, end="")


def main() -> NoReturn:
    """The project entry point.

    Returns:
        NoReturn: No return.
    """

    if len(argv) < 2:
        logger.error("You must specify a subcommand")
        exit(1)

    match argv[1]:
        case "run":
            x_run("./")
        case "create-readme-files":
            statistics_create_readme_files("./")
        case _:
            logger.error("The subcommand can only be 'run' or 'create-readme-files'")
            exit(1)

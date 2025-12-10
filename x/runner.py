"""The runner module."""

import subprocess

from pathlib import Path
from subprocess import CompletedProcess
from typing import List


def runner_run(solution_filepath: Path, solution_args: List[str]) -> str:
    """Run an executable Python script.

    Args:
        solution_filepath (Path): The executable Python script file path.
        solution_args (List[str]): The executable Python script arguments.

    Raises:
        Exception: The subprocess exception.

    Returns:
        str: The subprocess standard output.
    """

    solution_args_str = " ".join(solution_args)

    completed_process: CompletedProcess[bytes]
    try:
        completed_process = subprocess.run(
            f"{solution_filepath.absolute()} {solution_args_str}",
            shell=True,
            check=True,
            capture_output=True,
        )
    except Exception as e:
        raise e

    output = completed_process.stdout.decode()

    return output

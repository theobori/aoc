"""A bunch of helpers and names."""

from typing import Self
from pathlib import Path

from pydantic import BaseModel, model_validator, Field

AOC_MAX_DAYS = 25
AOC_LOWEST_YEAR = 2015
AOC_HIGHEST_YEAR = 2025
AOC_PARTS_AMOUNT = 2


class AOCSolutionMetadata(BaseModel):
    """This model represents a AoC solution metadatas."""

    year: int = Field(
        title="The Year",
        description="This is the value of the AoC year",
        gt=AOC_LOWEST_YEAR - 1,
        lt=AOC_HIGHEST_YEAR + 1,
    )
    day: int = Field(
        title="The Day",
        description="This is the value of the AoC day of the year",
        gt=0,
        lt=AOC_MAX_DAYS + 1,
    )
    part: int = Field(
        title="The Part",
        description="This is the value of the AoC part of the day",
        gt=0,
        lt=AOC_PARTS_AMOUNT + 1,
    )

    @model_validator(mode="after")
    def check_metadatas(self) -> Self:
        """Additional validation for the metadatas.

        Raises:
            ValueError: The metadatas is not valid.

        Returns:
            Self: The object instance itself.
        """

        highest_day_number = aoc_get_days_amount(self.year)
        if self.day > highest_day_number:
            raise ValueError(f"It cannot exceeds '{highest_day_number}'")

        return self


def aoc_get_days_amount(year: int) -> int:
    """Returns the days amount associated to a specific year.

    Args:
        year (int): The year.

    Returns:
        int: The days amount.
    """

    return 25 if year < 2025 else 12


def aoc_get_parts_amount(year: int) -> int:
    """Returns the parts amount associated to a specific year.

    Args:
        year (int): The year.

    Returns:
        int: The parts amount.
    """

    return aoc_get_days_amount(year) * 2


def aoc_get_directory_day_name(day: int) -> str:
    """Returns the standard name for an Advent Of Code day directory name.

    Args:
        day (int): The day.

    Returns:
        str: The directory name.
    """

    return f"{day:02}"


def aoc_get_file_part_name(part: int) -> str:
    """Returns the standard name for an Advent Of Code part file name.

    Args:
        day (int): The part.

    Returns:
        str: The directory name.
    """

    return f"part{part}.py"


def aoc_get_solution_filepath(
    directory_path: Path, aoc_solution_metadata: AOCSolutionMetadata
) -> Path:
    """Returns the solution file path.

    Args:
        directory_path (Path): The directory path.
        aoc_solution_metadata (AOCSolutionMetadata): The solution metadatas.

    Returns:
        Path: The solution file path.
    """

    return Path(
        directory_path,
        str(aoc_solution_metadata.year),
        aoc_get_directory_day_name(aoc_solution_metadata.day),
        aoc_get_file_part_name(aoc_solution_metadata.part),
    )

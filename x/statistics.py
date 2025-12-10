"""The statistics module."""

from typing import NoReturn, Dict, List
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass

from x.aoc import (
    aoc_get_directory_day_name,
    aoc_get_days_amount,
    AOC_PARTS_AMOUNT,
    aoc_get_file_part_name,
    aoc_get_parts_amount,
    AOC_LOWEST_YEAR,
    AOC_HIGHEST_YEAR,
)

from loguru import logger

STATISTICS_MARKDONW_TEMPLATE = """# My Advent Of Code statistics for {{year}}

I completed it **{{completion_percent}}% ({{parts_completed}}/{{parts_amount}})**, here's a table showing my problem-solving statistics for the year {{year}}.

{{table}}
"""

type StatisticsDay = List[bool]
type StatisticsYear = Dict[int, StatisticsDay]
type StatisticsDict = Dict[int, StatisticsYear]

type SolvedMetrics = Dict[int, int]


@dataclass(kw_only=True)
class Statistics:
    statistics: StatisticsDict
    # Amount of problems solved per year
    solved_metrics: SolvedMetrics


def statistics_create_from_directory(directory_path: Path = "./") -> Statistics:
    """Create a statistics object given a specific directory path.

    Args:
        directory_path (Path, optional): _description_. Defaults to "./".

    Returns:
        Statistics: The statistics object.
    """

    statistics: StatisticsDict = defaultdict(lambda: defaultdict(list))
    solved_metrics: SolvedMetrics = defaultdict(int)

    for year in range(AOC_LOWEST_YEAR, AOC_HIGHEST_YEAR + 1):
        directory_year = Path(directory_path, str(year))
        if directory_year.is_dir() is False:
            continue

        year = int(directory_year.name)
        days_amount = aoc_get_days_amount(year)

        for day in range(1, days_amount + 1):
            directory_day = directory_year / aoc_get_directory_day_name(day)

            if directory_day.is_dir() is False:
                statistics[year][day] = [False, False]
                continue

            for part in range(1, AOC_PARTS_AMOUNT + 1):
                file_part = directory_day / aoc_get_file_part_name(part)
                is_done = file_part.exists() and file_part.is_file()

                statistics[year][day].append(is_done)
                solved_metrics[year] += is_done

    return Statistics(
        statistics=statistics,
        solved_metrics=solved_metrics,
    )


def _statistics_create_markdown_table(statistics_year: StatisticsYear) -> str:
    """Returns the markdown table.

    Args:
        statistics_year (StatisticsYear): The statistics of a specific year.

    Returns:
        str: The markdown table.
    """

    if len(statistics_year) == 0:
        return ""

    lines = ["| Day | First part | Second part |", "| - | - | - |"]

    for day, parts in statistics_year.items():
        arr = [f"**{day}**"]
        for part in parts:
            arr.append("Yes" if part else "No")

        line = "| " + " | ".join(arr) + " |"

        lines.append(line)

    markdown_table = "\n".join(lines)

    return markdown_table


def _statistics_write_as_markdown(
    statistics: Statistics, directory_path: Path, filename: str = "README.md"
) -> NoReturn:
    """_summary_

    Args:
        statistics (Statistics): The statistics object instance.
        directory_path (Path): The directory path.
        filename (str, optional): The markdown filename. Defaults to "README.md".

    Returns:
        NoReturn: No return.
    """

    for year, statistics_year in statistics.statistics.items():
        year_str = str(year)

        markdown_table = _statistics_create_markdown_table(statistics_year)
        parts_amount = aoc_get_parts_amount(year)

        parts_completed = statistics.solved_metrics[year]
        completion_percent = (parts_completed / parts_amount) * 100

        readme = (
            STATISTICS_MARKDONW_TEMPLATE.replace("{{year}}", year_str)
            .replace("{{completion_percent}}", f"{completion_percent:02}")
            .replace("{{table}}", markdown_table)
            .replace("{{parts_completed}}", str(parts_completed))
            .replace("{{parts_amount}}", str(parts_amount))
        )
        readme_path = Path(directory_path, year_str, filename)

        with open(readme_path, "w+") as f:
            f.write(readme)

        logger.info(
            f"Written Advent Of Code statistics for {year_str} into {readme_path.absolute()}"
        )


def statistics_create_readme_files(directory_path: Path) -> NoReturn:
    """Create a README markdown file with problem-solving statistics.

    Args:
        directory_path (Path): The directory path.

    Returns:
        NoReturn: No return.
    """

    statistics = statistics_create_from_directory(directory_path)

    try:
        _statistics_write_as_markdown(statistics, directory_path)
    except Exception as e:
        raise e

"""Module to get the puzzle input, either passed as an
argument via the CLI (path to the puzzle input file)
or from standard in."""
import io
import os
import pathlib
import sys

from typing import List

from aoc2023._cli import _collect_cli_args


def _have_content_from_stdin() -> bool:
    # pytest capture raises.
    try:
        stdin_content_present = not os.isatty(sys.stdin.fileno())
    except io.UnsupportedOperation:
        stdin_content_present = False
    return stdin_content_present


def _have_input_file_and_exists(input_file_path: str | None) -> bool:
    """Check if the file is a file and is readable. If None is provided,
    False is returned.

    :param input_file_path: Possible input file path.
    :returns: Bool indicating if the input file exists and is readable.
    :raises: OSError"""
    if not input_file_path:
        return False
    file_path = pathlib.Path(input_file_path)
    if not file_path.is_file():
        raise OSError(f"Provided file {str(file_path)} is not a file.")
    if not os.access(file_path, os.R_OK):
        raise OSError(f"Provided file {str(file_path)} is a file, but is not readable.")
    return True


def get_puzzle_input(args: List[str]) -> List[str]:
    """Get puzzle input from file passed via CLI or from standard in.

    :param args: Command line arguments.
    :returns: List of lines in input file.
    :raises: RuntimeError"""
    input_file_path_from_cli = _collect_cli_args(args)

    if _have_content_from_stdin() and not _have_input_file_and_exists(
        input_file_path_from_cli
    ):
        input = list(map(str.strip, sys.stdin.readlines()))  # stdin
    elif not _have_content_from_stdin() and _have_input_file_and_exists(
        input_file_path_from_cli
    ):
        with open(input_file_path_from_cli, "r") as f:
            input = list(map(str.strip, f.readlines()))  # file arg
    elif _have_content_from_stdin() and _have_input_file_and_exists(
        input_file_path_from_cli
    ):
        raise RuntimeError(
            "Encountered both input from standard in and "
            "input file from CLI. Expected only input from "
            "standard in or file specified at the CLI."
        )
    else:
        raise RuntimeError(
            "Did not encounter input from standard in or input "
            "file from CLI. Expected input from standard in or "
            "file specified at the CLI."
        )
    return input

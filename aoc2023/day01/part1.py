import sys

from typing import List

from aoc2023._getinput import get_puzzle_input


def remove_letters_from_string(s: str) -> str:
    """Remove all non-digit characters from a string, leaving behind only digits (0-9).

    :param s: String to remove non-digit characters from.
    :returns: Empty string or string containing only digits."""
    return "".join(filter(lambda c: c.isdigit(), s))


def first_last_digit_concat_int(digit_only_string: str) -> int:
    """Create a new double-digit number, with the tens place being the first digit
    encountered in the provided string and the ones place being the last digit
    encountered.

    :param digit_only_string: String expected to contain only digits.
    :returns: One integer that can be [0,99].
    :raises: ValueError"""
    if not digit_only_string.isdigit():
        raise ValueError(
            f"Function {first_last_digit_concat_int.__qualname__} was provided a string "
            f"containing no digits. Encountered '{digit_only_string}', "
            "but expected a string containing at least one digit."
        )

    return int(f"{digit_only_string[0]}{digit_only_string[-1]}")


def _main(args: List[str] = sys.argv[1:]) -> None:
    input_lines = get_puzzle_input(args)
    input_lines_only_numbers = list(map(remove_letters_from_string, input_lines))
    concat_int_list = list(map(first_last_digit_concat_int, input_lines_only_numbers))

    print(sum(concat_int_list))

import re
import sys

from typing import List, Match

from aoc2023._getinput import get_puzzle_input


def get_numbers_beside_symbols(schematic_lines: List[str]) -> List[int]:
    """Iterate over each row of the schematic lines, identify all numbers
    that are next to a symbol. Return the list of numbers.

    :param: schematic_lines: List of schematic input lines.
    :returns: List of numbers adjacent to a symbol."""
    valid_numbers = []
    for row_idx, row in enumerate(schematic_lines):
        valid_numbers.extend(
            [
                int(m.group())
                for m in re.finditer(r"[0-9]+", row)
                if _match_has_adjacent_symbol(m, row_idx, schematic_lines)
            ]
        )
    return valid_numbers


def _match_has_adjacent_symbol(
    matched_str: Match[str], row_idx: int, schematic_lines: List[str]
) -> bool:
    """Using Match context information, see if the number captured by
    the Match has a symbol near it.

    :param matched_str: Match of a number in a row from schematic_lines.
    :param row_idx: Row the number was matched on.
    :param schematic_lines: List of schematic input lines."""
    for int_idx in range(matched_str.start(), matched_str.end()):
        for x_shift in range(-1, 2):
            for y_shift in range(-1, 2):
                try:
                    if re.search(
                        r"^[^0-9a-zA-Z\.]{1}$",
                        schematic_lines[row_idx + y_shift][int_idx + x_shift],
                    ):
                        return True
                except IndexError:
                    pass
    return False


def _main(args: List[str] = sys.argv[1:]) -> None:
    input_lines = get_puzzle_input(args)
    numbers_beide_symbols = get_numbers_beside_symbols(input_lines)

    print(sum(numbers_beide_symbols))

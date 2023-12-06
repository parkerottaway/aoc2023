import re
import sys

from typing import List

from aoc2023._getinput import get_puzzle_input
from aoc2023.day01.part1 import first_last_digit_concat_int, remove_letters_from_string


def digit_names_to_symbols(input: str) -> str:
    """Accepts a string and returns a new string with
    the digit names replaced with the symbol (e.g., a
    string containing the substring 'two' will have every
    instance of 'two' replaced with '2'). Overlapping
    instances of digit names will also be substituted
    (e.g., 'oneight' will be replaced with '18').

    :param input: Input string to replace all instances of digit names.
    :returns: Empty string, the original string, or a new string with
              digit names replaced in the old string"""
    combo_name_to_digit_mapping = {
        "oneigh(?=t)": "oneeigh",
        "twon(?=e)": "twoon",
        "threeigh(?=t)": "threeeigh",
        "fiveigh(?=t)": "fiveeigh",
        "sevenin(?=e)": "sevennin",
        "eightw(?=o)": "eighttw",
        "eighthre(?=e)": "eightthre",
        "nineigh(?=t)": "nineeigh",
    }
    name_to_digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    combo_digits_split = str(input)
    for pattern, replacement in combo_name_to_digit_mapping.items():
        combo_digits_split = re.sub(pattern, replacement, combo_digits_split)
    return re.sub(
        "|".join([*name_to_digit_mapping]),
        lambda x: name_to_digit_mapping[x.group(0)],
        combo_digits_split,
    )


def _main(args: List[str] = sys.argv[1:]) -> None:
    input_lines = get_puzzle_input(args)
    input_lines_digit_names_replaced = list(map(digit_names_to_symbols, input_lines))
    input_lines_only_numbers = list(
        map(remove_letters_from_string, input_lines_digit_names_replaced)
    )
    concat_int_list = list(map(first_last_digit_concat_int, input_lines_only_numbers))

    print(sum(concat_int_list))

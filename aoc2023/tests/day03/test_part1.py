import pathlib
import pytest
import re

from aoc2023.day03.part1 import (
    _main,
    _match_has_adjacent_symbol,
    get_numbers_beside_symbols,
)


def test_validPuzzleInput_returnsExpectedListOfIntegers():
    assert get_numbers_beside_symbols([]) == []
    assert get_numbers_beside_symbols(["."]) == []
    assert get_numbers_beside_symbols(["*"]) == []
    assert get_numbers_beside_symbols(["2"]) == []
    assert get_numbers_beside_symbols(["...2..."]) == []
    assert get_numbers_beside_symbols(["..*2..."]) == [2]
    assert get_numbers_beside_symbols(["...2...", "...&..."]) == [2]
    assert get_numbers_beside_symbols(["...2...", "....^.."]) == [2]
    assert get_numbers_beside_symbols(["...2...", ".....%."]) == []
    assert get_numbers_beside_symbols(
        [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
    ) == [467, 35, 633, 617, 592, 755, 664, 598]


def test_matchAdjacentSymbolTest_returnsExpectedValue():
    input_passing_check = ["...2...", "...&..."]
    input_passing_check_row_with_number = 0
    assert _match_has_adjacent_symbol(
        re.search(r"[0-9]+", input_passing_check[input_passing_check_row_with_number]),
        input_passing_check_row_with_number,
        input_passing_check,
    )

    input_not_passing_check = ["...2...", ".....%."]
    input_not_passing_check_row_with_number = 0
    assert not _match_has_adjacent_symbol(
        re.search(
            r"[0-9]+", input_not_passing_check[input_not_passing_check_row_with_number]
        ),
        input_not_passing_check_row_with_number,
        input_not_passing_check,
    )


@pytest.mark.skipif(
    (
        not (
            pathlib.Path(__file__).parent.parent.parent.parent
            / "secrets"
            / "day03"
            / "input.txt"
        ).is_file()
    )
    or (
        not (
            pathlib.Path(__file__).parent.parent.parent.parent
            / "secrets"
            / "day03"
            / "part1.soln"
        ).is_file()
    ),
    reason="Puzzle input or solution not available on filesystem.",
)
def test_puzzleInput_returnsExpectedAnswer(capsys):
    puzzle_input_file = (
        pathlib.Path(__file__).parent.parent.parent.parent
        / "secrets"
        / "day03"
        / "input.txt"
    )
    puzzle_solution_file = (
        pathlib.Path(__file__).parent.parent.parent.parent
        / "secrets"
        / "day03"
        / "part1.soln"
    )
    with open(puzzle_solution_file, "r") as f:
        expected_output = f.readline()

    _main([str(puzzle_input_file)])
    stdout = capsys.readouterr().out.strip()
    test_result = expected_output == stdout
    assert test_result

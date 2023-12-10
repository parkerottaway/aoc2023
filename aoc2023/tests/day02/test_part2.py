import pathlib
import pytest

from aoc2023.day02.game import BlockColorsSet
from aoc2023.day02.part2 import calculate_cube_set_power, _main


def test_powerCalculationWithValidInput_returnsExpectedResult():
    assert 0 == calculate_cube_set_power(BlockColorsSet(red=0, green=1, blue=1))
    assert 1 == calculate_cube_set_power(BlockColorsSet(red=1, green=1, blue=1))


@pytest.mark.skipif(
    (
        not (
            pathlib.Path(__file__).parent.parent.parent.parent
            / "secrets"
            / "day02"
            / "input.txt"
        ).is_file()
    )
    or (
        not (
            pathlib.Path(__file__).parent.parent.parent.parent
            / "secrets"
            / "day02"
            / "part2.soln"
        ).is_file()
    ),
    reason="Puzzle input or solution not available on filesystem.",
)
def test_puzzleInput_returnsExpectedAnswer(capsys):
    puzzle_input_file = (
        pathlib.Path(__file__).parent.parent.parent.parent
        / "secrets"
        / "day02"
        / "input.txt"
    )
    puzzle_solution_file = (
        pathlib.Path(__file__).parent.parent.parent.parent
        / "secrets"
        / "day02"
        / "part2.soln"
    )
    with open(puzzle_solution_file, "r") as f:
        expected_output = f.readline()

    _main([str(puzzle_input_file)])
    stdout = capsys.readouterr().out.strip()
    test_result = expected_output == stdout
    assert test_result

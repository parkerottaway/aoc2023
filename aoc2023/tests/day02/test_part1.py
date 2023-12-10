import pathlib
import pytest

from aoc2023.day02.game import BlockColorsSet
from aoc2023.day02.part1 import cube_set_ceiling_met, _main


def test_cubeCeiling_enforcesCeiling():
    assert cube_set_ceiling_met(
        BlockColorsSet(red=10, green=9, blue=8),
        BlockColorsSet(red=10, green=10, blue=10),
    )
    assert not cube_set_ceiling_met(
        BlockColorsSet(red=10, green=9, blue=8), BlockColorsSet(red=1, green=1, blue=1)
    )
    assert cube_set_ceiling_met(
        BlockColorsSet(red=1, green=9, blue=8),
        BlockColorsSet(red=None, green=10, blue=10),
    )
    assert cube_set_ceiling_met(
        BlockColorsSet(red=None, green=9, blue=8),
        BlockColorsSet(red=1, green=10, blue=10),
    )

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
            / "part1.soln"
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
        / "part1.soln"
    )
    with open(puzzle_solution_file, "r") as f:
        expected_output = f.readline()

    _main([str(puzzle_input_file)])
    stdout = capsys.readouterr().out.strip()
    test_result = expected_output == stdout
    assert test_result

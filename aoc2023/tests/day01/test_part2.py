import pathlib
import pytest

from aoc2023.day01.part2 import digit_names_to_symbols, _main


def test_digitNamesToSymbols_individualDigitsEnteredCorrectly():
    assert digit_names_to_symbols("one") == "1"
    assert digit_names_to_symbols("two") == "2"
    assert digit_names_to_symbols("three") == "3"
    assert digit_names_to_symbols("four") == "4"
    assert digit_names_to_symbols("five") == "5"
    assert digit_names_to_symbols("six") == "6"
    assert digit_names_to_symbols("seven") == "7"
    assert digit_names_to_symbols("eight") == "8"
    assert digit_names_to_symbols("nine") == "9"


def test_digitNamesToSymbols_allDigitNamesReplacedWithSymbols():
    assert digit_names_to_symbols("") == ""
    assert digit_names_to_symbols("two1nine") == "219"
    assert digit_names_to_symbols("eightwothree") == "823"
    assert digit_names_to_symbols("abcone2threexyz") == "abc123xyz"
    assert digit_names_to_symbols("xtwone3four") == "x2134"
    assert digit_names_to_symbols("4nineeightseven2") == "49872"
    assert digit_names_to_symbols("zoneight234") == "z18234"
    assert digit_names_to_symbols("7pqrstsixteen") == "7pqrst6teen"
    assert (
        digit_names_to_symbols("pveightwothree2kfzpkks3ljxnbp")
        == "pv8232kfzpkks3ljxnbp"
    )
    assert (
        digit_names_to_symbols("388eightkrmdktwopjdlpfmfivetwoneql")
        == "3888krmdk2pjdlpfm521ql"
    )
    assert digit_names_to_symbols("twotwotwotwo") == "2222"
    assert digit_names_to_symbols("threeighthree") == "383"


@pytest.mark.skipif(
    (
        not (
            pathlib.Path(__file__).parent.parent.parent.parent
            / "secrets"
            / "day01"
            / "input.txt"
        ).is_file()
    )
    or (
        not (
            pathlib.Path(__file__).parent.parent.parent.parent
            / "secrets"
            / "day01"
            / "part2.soln"
        ).is_file()
    ),
    reason="Puzzle input or solution not available on filesystem.",
)
def test_puzzleInput_returnsExpectedAnswer(capsys):
    puzzle_input_file = (
        pathlib.Path(__file__).parent.parent.parent.parent
        / "secrets"
        / "day01"
        / "input.txt"
    )
    puzzle_solution_file = (
        pathlib.Path(__file__).parent.parent.parent.parent
        / "secrets"
        / "day01"
        / "part2.soln"
    )
    with open(puzzle_solution_file, "r") as f:
        expected_output = f.readline()

    _main([str(puzzle_input_file)])
    stdout = capsys.readouterr().out.strip()
    test_result = expected_output == stdout
    assert test_result

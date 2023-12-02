import pathlib
import pytest

from aoc2023.day01.part1 import (
    first_last_digit_concat_int,
    remove_letters_from_string,
    _main,
)


def test_nonDigitFiltering_returnsDigitsOrEmptyString():
    assert remove_letters_from_string("") == ""
    assert remove_letters_from_string("1abc2") == "12"
    assert remove_letters_from_string("pqr3stu8vwx") == "38"
    assert remove_letters_from_string("a1b2c3d4e5f") == "12345"
    assert remove_letters_from_string("treb7uchet") == "7"
    assert remove_letters_from_string("trebuchet") == ""
    assert remove_letters_from_string("** trebuchet") == ""
    assert remove_letters_from_string("2\n\ttrebuchet") == "2"
    assert remove_letters_from_string("4\x07trebuchet") == "4"
    assert remove_letters_from_string("\U000002916trebuchet") == "6"


def test_concatIntegerResult_createsNewExpectedInteger():
    assert first_last_digit_concat_int("0") == 0
    assert first_last_digit_concat_int("01") == 1
    assert first_last_digit_concat_int("10") == 10
    assert first_last_digit_concat_int("0000000000") == 0
    assert first_last_digit_concat_int("9999999999") == 99
    assert first_last_digit_concat_int("1234567890") == 10
    assert first_last_digit_concat_int("987654321") == 91


def test_concatIntegerResult_raisesValueErrorForUnsupportedInput():
    with pytest.raises(ValueError) as ec:
        _ = first_last_digit_concat_int("")
    assert ec.value.args[0].startswith(
        f"Function {first_last_digit_concat_int.__qualname__}"
    )

    with pytest.raises(ValueError):
        _ = first_last_digit_concat_int("")
        _ = first_last_digit_concat_int("a")
        _ = first_last_digit_concat_int("111a111")


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
            / "part1.soln"
        ).is_file()
    ),
    reason="Puzzle input or solution not available on filesystem.",
)
def test_puzzleSolution_returnsExpectedAnswer(capsys):
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
        / "part1.soln"
    )
    with open(puzzle_solution_file, "r") as f:
        expected_output = f.readline()

    _main([str(puzzle_input_file)])
    stdout = capsys.readouterr().out.strip()
    test_result = expected_output == stdout
    assert test_result

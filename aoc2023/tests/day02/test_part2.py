from aoc2023.day02.game import BlockColorsSet
from aoc2023.day02.part2 import calculate_cube_set_power


def test_powerCalculationWithValidInput_returnsExpectedResult():
    assert 0 == calculate_cube_set_power(BlockColorsSet(red=0, green=1, blue=1))
    assert 1 == calculate_cube_set_power(BlockColorsSet(red=1, green=1, blue=1))

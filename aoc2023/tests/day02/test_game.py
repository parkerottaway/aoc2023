import pytest

from aoc2023.day02.game import BlockColorsSet, Game


def test_blockListBuilderEmptyArg_raisesValueError():
    with pytest.raises(ValueError) as ec:
        _ = Game("Game 1:")
    assert ec.value.args[0] == "Did not encounter block color counts."


def test_newGameInstantiatedWithValidGameString_returnsObjectWithExpectedFields():
    g = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert g.id == 1
    assert g.block_counts == BlockColorsSet(red=4, blue=6, green=2)

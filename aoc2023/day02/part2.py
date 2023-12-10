import sys

from typing import List

from aoc2023._getinput import get_puzzle_input
from aoc2023.day02.game import BlockColorsSet, Game


def calculate_cube_set_power(bcs: BlockColorsSet) -> int:
    return (
        (bcs.red if bcs.red else 0)
        * (bcs.green if bcs.green else 0)
        * (bcs.blue if bcs.blue else 0)
    )


def _main(args: List[str] = sys.argv[1:]) -> None:
    input_lines = get_puzzle_input(args)
    game_powers = [calculate_cube_set_power(Game(l).block_counts) for l in input_lines]

    print(sum(game_powers))

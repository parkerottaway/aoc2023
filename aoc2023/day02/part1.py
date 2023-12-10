import sys

from typing import List

from aoc2023._getinput import get_puzzle_input
from aoc2023.day02.game import BlockColorsSet, Game


def cube_set_ceiling_met(cube_set: BlockColorsSet, ceiling: BlockColorsSet) -> bool:
    """Check if the provided cube set has all cube color counts at or below the
    provided ceiling counts. A cube color count of None is to be interpreted as
    infinity.

    :param cube_set: Cube color counts to check.
    :param ceiling: Cube color counts to compare against.
    :returns: Boolean indicating whether or not the cube set meets the
              ceiling restriction."""
    check_color = (
        lambda s, c, a: (
            (not getattr(c, a)) and getattr(s, a)
        )  # no ceiling defined, but color encountered
        or (not getattr(s, a))  # color not encountered
        or (getattr(s, a) <= getattr(c, a))  # count under ceiling
    )
    return (
        check_color(cube_set, ceiling, "red")
        and check_color(cube_set, ceiling, "green")
        and check_color(cube_set, ceiling, "blue")
    )


def _main(args: List[str] = sys.argv[1:]) -> None:
    input_lines = get_puzzle_input(args)
    cube_set_ceiling = BlockColorsSet(red=12, green=13, blue=14)
    game_ids_meeting_ceiling = [
        g.id
        for l in input_lines
        if cube_set_ceiling_met((g := Game(l)).block_counts, cube_set_ceiling)
    ]

    print(sum(game_ids_meeting_ceiling))

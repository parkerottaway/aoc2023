from collections import namedtuple
from typing import List, Tuple


BlockColorsSet = namedtuple("BlockColorSet", ["red", "green", "blue"])
BlockColorsSet.__doc__ = """\
Set of colors encountered. Tuple elements may be integers or
None, where None, is to be interpreted as infinity.

:param red: Number of red blocks.
:type red: integer or None.
:param green: Number of green blocks.
:type green: integer or None.
:param blue: Number of blue blocks.
:type blue: integer or None."""


class Game:
    """Reports important aspects of a game, such as the game ID and the
    largest numbers of each color block encountered during the game."""

    def __init__(self, game_str: str):
        game_str_stack = list(reversed(game_str.strip().split()))
        _ = game_str_stack.pop()  # remove 'Game'
        self.id = int(game_str_stack.pop().strip(":"))
        self.block_counts = self._find_largest_color_counts(game_str_stack)

    def _build_block_color_count_lists(
        self,
        gs: List[str],
    ) -> Tuple[List[str], List[str], List[str]]:
        """Process the stack of color cube draws and return the list of number
        of cubes drawn for each color cube.

        :param gs: Game string stack with 'Game ###:' removed.
        :returns: Three lists, each list holds the number of blocks encountered
                  for each pull of one game.
        :raises: ValueError"""
        if not gs:
            raise ValueError("Did not encounter block color counts.")
        reds, blues, greens = [], [], []
        while gs:
            count = int(gs.pop())
            color = gs.pop().strip(",;")  # e.g., 'blue', 'blue,', 'blue;'
            match color:
                case "red":
                    reds.insert(0, count)
                case "green":
                    greens.insert(0, count)
                case "blue":
                    blues.insert(0, count)
                case _:
                    raise ValueError(
                        "Encountered unsupported color "
                        f"'{color}'. Expected 'red', "
                        "'green', or 'blue'."
                    )
        return reds, blues, greens

    def _find_largest_color_counts(self, gs: List[str]) -> BlockColorsSet:
        """Return the largest number of blocks seen in a single
        draw during one one.

        :param gs: Game string stack with 'Game ###:' removed.
        :returns: Set of color counts representing the largest number of
                  blocks observed in the game."""
        reds, blues, greens = self._build_block_color_count_lists(gs)
        bcs = BlockColorsSet(
            red=sorted(reds)[-1] if reds else None,
            green=sorted(greens)[-1] if greens else None,
            blue=sorted(blues)[-1] if blues else None,
        )
        return bcs

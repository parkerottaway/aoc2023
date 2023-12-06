"""Common command line interface functionality to be
shared across each part of each day's challenge executables."""
import argparse

from typing import List


def _add_optional_file_input_arg(ap: argparse.ArgumentParser) -> None:
    _ = ap.add_argument(
        "filename",
        action="store",
        nargs="?",
        help="path to input file containing puzzle input",
        metavar="FILE",
    )


def _build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Command line interface for accepting an optional file "
        "path. Input file content may also be provided via "
        "standard in."
    )
    _add_optional_file_input_arg(parser)

    return parser


def _collect_cli_args(args: List[str]) -> str:
    ap = _build_argument_parser()
    ns = ap.parse_args(args)

    return ns.filename

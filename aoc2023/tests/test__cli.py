import pytest

from aoc2023._cli import _build_argument_parser, _collect_cli_args


def test_argumentConfiguration_onlyAllowsSupportedConfig():
    _ = _build_argument_parser().parse_args([])
    _ = _build_argument_parser().parse_args(["/file/that/does/not/exist.txt"])

    with pytest.raises(SystemExit):
        _ = _build_argument_parser().parse_args(
            ["/file/that/does/not/exist.txt", "/other/file/that/does/not/exist.txt"]
        )


def test_argumentCollection_onlySupportedConfigsAndReturnExpectedValues():
    assert _collect_cli_args([]) == None
    assert (
        _collect_cli_args(["/file/that/does/not/exist.txt"])
        == "/file/that/does/not/exist.txt"
    )

    with pytest.raises(SystemExit):
        _ = _collect_cli_args(
            ["/file/that/does/not/exist.txt", "/other/file/that/does/not/exist.txt"]
        )

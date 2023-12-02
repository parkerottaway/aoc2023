import pytest

from aoc2023._getinput import get_puzzle_input, _have_input_file_and_exists

_READABLE_DIR = "/etc"
_UNREADABLE_FILE = "/etc/sudoers"
_READABLE_FILE = "/etc/bashrc"


def test_unsupportedInputCheck_raisesExceptionOrPasses():
    _ = _have_input_file_and_exists(_READABLE_FILE)

    with pytest.raises(OSError) as ec:
        _ = _have_input_file_and_exists(_READABLE_DIR)
    assert ec.value.args[0].endswith("is not a file.")

    with pytest.raises(OSError) as ec:
        _ = _have_input_file_and_exists(_UNREADABLE_FILE)
    assert ec.value.args[0].endswith("is not readable.")


def test_collectInputFromCLIAttempt_raisesExceptionOrPasses():
    _ = get_puzzle_input([_READABLE_FILE])

    with pytest.raises(OSError) as ec:
        _ = get_puzzle_input([_READABLE_DIR])
    assert ec.value.args[0].endswith("is not a file.")

    with pytest.raises(OSError) as ec:
        _ = get_puzzle_input([_UNREADABLE_FILE])
    assert ec.value.args[0].endswith("is not readable.")

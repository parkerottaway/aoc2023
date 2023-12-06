import pathlib
import pytest

from aoc2023._getinput import get_puzzle_input, _have_input_file_and_exists

_DIR_CONTAINING_THIS_MODULE = pathlib.Path(__file__).parent


@pytest.fixture()
def readable_dir() -> str:
    dir = _DIR_CONTAINING_THIS_MODULE / "tempdir"
    dir.mkdir(mode=0o755, exist_ok=True)
    yield str(dir)
    dir.rmdir()


@pytest.fixture()
def unreadable_file() -> str:
    file = _DIR_CONTAINING_THIS_MODULE / "unreadable_file.txt"
    file.touch(mode=0o000, exist_ok=True)
    yield str(file)
    file.unlink()


@pytest.fixture()
def readable_file() -> str:
    file = _DIR_CONTAINING_THIS_MODULE / "readable_file.txt"
    file.touch(mode=0o644, exist_ok=True)
    yield str(file)
    file.unlink()


def test_unsupportedInputCheck_raisesExceptionOrPasses(
    readable_file, readable_dir, unreadable_file
):
    _ = _have_input_file_and_exists(readable_file)

    with pytest.raises(OSError) as ec:
        _ = _have_input_file_and_exists(readable_dir)
    assert ec.value.args[0].endswith("is not a file.")

    with pytest.raises(OSError) as ec:
        _ = _have_input_file_and_exists(unreadable_file)
    assert ec.value.args[0].endswith("is not readable.")


def test_collectInputFromCLIAttempt_raisesExceptionOrPasses(
    readable_file, readable_dir, unreadable_file
):
    _ = get_puzzle_input([readable_file])

    with pytest.raises(OSError) as ec:
        _ = get_puzzle_input([readable_dir])
    assert ec.value.args[0].endswith("is not a file.")

    with pytest.raises(OSError) as ec:
        _ = get_puzzle_input([unreadable_file])
    assert ec.value.args[0].endswith("is not readable.")

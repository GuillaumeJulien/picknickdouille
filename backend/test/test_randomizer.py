import pytest

from ..main import Randomizer


def test_randomizer_return_list_with_same_names():
    names = ["foo", "bar", "baz"]
    rand = Randomizer()
    result = rand.get_list_names(names)
    assert len(result) == len(names)
    assert sorted(result) == sorted(names)

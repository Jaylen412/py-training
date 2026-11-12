import importlib
import os
from typing import Optional, get_type_hints

import pytest

mod = importlib.import_module(
    "sol_11_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_11_02"
)


def test_mean():
    assert mod.mean([1.0, 2.0, 6.0]) == pytest.approx(3.0)
    assert mod.mean([]) == 0.0


def test_mean_hints():
    assert get_type_hints(mod.mean) == {"values": list[float], "return": float}


def test_word_lengths():
    assert mod.word_lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}
    assert mod.word_lengths([]) == {}


def test_word_lengths_hints():
    assert get_type_hints(mod.word_lengths) == {"words": list[str], "return": dict[str, int]}


def test_first_long_word():
    assert mod.first_long_word(["a", "abc", "abcd"], 3) == "abc"
    assert mod.first_long_word(["a", "b"], 3) is None


def test_first_long_word_hints():
    # Optional[str] and str | None are the same type, so either spelling passes.
    hints = get_type_hints(mod.first_long_word)
    assert hints == {"words": list[str], "minimum": int, "return": Optional[str]}


def test_split_pair():
    assert mod.split_pair("name, Ada") == ("name", "Ada")
    assert mod.split_pair("a=b=c", separator="=") == ("a", "b=c")


def test_split_pair_missing_separator():
    with pytest.raises(ValueError):
        mod.split_pair("no comma here")


def test_split_pair_hints():
    hints = get_type_hints(mod.split_pair)
    assert hints == {"text": str, "separator": str, "return": tuple[str, str]}

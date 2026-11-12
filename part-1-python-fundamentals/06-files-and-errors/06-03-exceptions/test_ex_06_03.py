import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_06_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_06_03"
)


def test_safe_divide():
    assert mod.safe_divide(6, 3) == pytest.approx(2.0)


def test_safe_divide_by_zero():
    assert mod.safe_divide(6, 0) is None
    assert mod.safe_divide(0, 0) is None


def test_to_int_or_default():
    assert mod.to_int_or_default("12") == 12
    assert mod.to_int_or_default(" -3 ") == -3


def test_to_int_or_default_bad_text():
    assert mod.to_int_or_default("twelve") == 0
    assert mod.to_int_or_default("twelve", default=-1) == -1
    assert mod.to_int_or_default("") == 0


def test_read_text_or_empty(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("hello\n")
    assert mod.read_text_or_empty(path) == "hello\n"


def test_read_text_or_empty_missing(tmp_path):
    assert mod.read_text_or_empty(tmp_path / "missing.txt") == ""


def test_parse_numbers():
    assert mod.parse_numbers(["1", "x", "2.5"]) == ([1.0, 2.5], ["x"])


def test_parse_numbers_empty_and_all_bad():
    assert mod.parse_numbers([]) == ([], [])
    assert mod.parse_numbers(["a", ""]) == ([], ["a", ""])


def test_load_json_or_default_valid(tmp_path):
    path = tmp_path / "data.json"
    path.write_text('{"a": 1}')
    assert mod.load_json_or_default(path, {}) == {"a": 1}


def test_load_json_or_default_missing(tmp_path):
    assert mod.load_json_or_default(tmp_path / "missing.json", []) == []


def test_load_json_or_default_corrupt(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("not json")
    assert mod.load_json_or_default(path, {"empty": True}) == {"empty": True}

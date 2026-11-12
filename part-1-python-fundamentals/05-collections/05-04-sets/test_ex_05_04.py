import importlib
import os

mod = importlib.import_module(
    "sol_05_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_05_04"
)


def test_unique_count():
    assert mod.unique_count(["a", "b", "a"]) == 2


def test_unique_count_empty():
    assert mod.unique_count([]) == 0


def test_has_duplicates():
    assert mod.has_duplicates([1, 2, 3, 2]) is True
    assert mod.has_duplicates([1, 2, 3]) is False


def test_has_duplicates_empty():
    assert mod.has_duplicates([]) is False


def test_common_items():
    assert mod.common_items([3, 1, 2, 2], [2, 3, 4]) == [2, 3]


def test_common_items_none_shared():
    assert mod.common_items([1], [2]) == []


def test_only_in_first():
    assert mod.only_in_first(["a", "b", "c"], ["b"]) == ["a", "c"]


def test_only_in_first_ignores_extra_in_second():
    assert mod.only_in_first([1, 1, 2], [2, 3, 4]) == [1]
    assert mod.only_in_first([], [1]) == []


def test_missing_fields():
    record = {"name": "Ada"}
    assert mod.missing_fields(record, ["name", "email", "age"]) == ["age", "email"]


def test_missing_fields_none_missing():
    record = {"name": "Ada", "email": "ada@example.com"}
    assert mod.missing_fields(record, ["name", "email"]) == []


def test_is_pangram():
    assert mod.is_pangram("The quick brown fox jumps over the lazy dog") is True


def test_is_pangram_missing_letter():
    assert mod.is_pangram("The quick brown fox jumps over the lazy cat") is False
    assert mod.is_pangram("") is False

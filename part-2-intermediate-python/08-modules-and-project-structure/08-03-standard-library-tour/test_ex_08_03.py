import importlib
import os

mod = importlib.import_module(
    "sol_08_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_08_03"
)


def test_days_between():
    assert mod.days_between("2026-11-11", "2026-12-25") == 44


def test_days_between_across_leap_day_and_backwards():
    assert mod.days_between("2028-02-28", "2028-03-01") == 2
    assert mod.days_between("2026-01-10", "2026-01-01") == -9
    assert mod.days_between("2026-01-01", "2026-01-01") == 0


def test_weekday_name():
    assert mod.weekday_name("2026-11-11") == "Wednesday"
    assert mod.weekday_name("2026-03-14") == "Saturday"


def test_top_words():
    assert mod.top_words("the cat and THE hat and the bat", 2) == [("the", 3), ("and", 2)]


def test_top_words_more_than_available():
    assert mod.top_words("a b", 5) == [("a", 1), ("b", 1)]
    assert mod.top_words("", 3) == []


def test_group_by_length():
    assert mod.group_by_length(["hi", "hey", "yo"]) == {2: ["hi", "yo"], 3: ["hey"]}


def test_group_by_length_returns_plain_dict():
    result = mod.group_by_length([])
    assert result == {}
    assert type(result) is dict


def test_all_pairs():
    assert mod.all_pairs(["a", "b", "c"]) == [("a", "b"), ("a", "c"), ("b", "c")]


def test_all_pairs_too_few_items():
    assert mod.all_pairs(["a"]) == []
    assert mod.all_pairs([]) == []


def test_roll_dice_known_seed():
    assert mod.roll_dice(3, 42) == [6, 1, 1]


def test_roll_dice_repeatable_and_in_range():
    first = mod.roll_dice(100, 7)
    assert first == mod.roll_dice(100, 7)
    assert all([1 <= roll <= 6 for roll in first])
    assert mod.roll_dice(0, 1) == []

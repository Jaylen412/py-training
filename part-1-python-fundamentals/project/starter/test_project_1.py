"""Tests for the Part 1 project. Run from the repository root with:

    python -m pytest part-1-python-fundamentals/project/starter

Set COURSE_SOLUTIONS=1 to run the same tests against the reference solution.
"""
import json
import os
import sys
from pathlib import Path

import pytest

if os.environ.get("COURSE_SOLUTIONS"):
    sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))

import expense_tracker as tracker  # noqa: E402

LUNCH = {"date": "2026-01-05", "category": "food", "amount": 12.5, "note": "lunch"}
BUS = {"date": "2026-01-20", "category": "transport", "amount": 2.4, "note": "bus"}
DINNER = {"date": "2026-02-02", "category": "food", "amount": 30.0, "note": ""}
EXPENSES = [LUNCH, BUS, DINNER]


# Requirement 1: validate_date

def test_validate_date_accepts_valid_dates():
    assert tracker.validate_date("2026-01-05") == "2026-01-05"
    assert tracker.validate_date(" 2026-12-31 ") == "2026-12-31"


@pytest.mark.parametrize("bad", ["2026/01/05", "26-01-05", "2026-1-5", "2026-13-01", "2026-00-10", "2026-01-32", "abcd-ef-gh", ""])
def test_validate_date_rejects_bad_dates(bad):
    with pytest.raises(ValueError):
        tracker.validate_date(bad)


# Requirement 2: parse_amount

def test_parse_amount():
    assert tracker.parse_amount("12.5") == 12.5
    assert tracker.parse_amount(" 3.456 ") == 3.46


@pytest.mark.parametrize("bad", ["abc", "", "0", "-4"])
def test_parse_amount_rejects_bad_amounts(bad):
    with pytest.raises(ValueError):
        tracker.parse_amount(bad)


# Requirement 3: make_expense

def test_make_expense_cleans_values():
    expense = tracker.make_expense("2026-01-05", "  Food ", "12.50", " lunch ")
    assert expense == LUNCH


def test_make_expense_note_is_optional():
    assert tracker.make_expense("2026-02-02", "food", "30")["note"] == ""


def test_make_expense_rejects_empty_category():
    with pytest.raises(ValueError):
        tracker.make_expense("2026-01-05", "   ", "5", "")


# Requirement 4: add_expense

def test_add_expense_returns_new_list():
    original = [LUNCH]
    result = tracker.add_expense(original, BUS)
    assert result == [LUNCH, BUS]
    assert original == [LUNCH]


# Requirement 5: filter_by_category

def test_filter_by_category():
    assert tracker.filter_by_category(EXPENSES, "food") == [LUNCH, DINNER]
    assert tracker.filter_by_category(EXPENSES, " FOOD ") == [LUNCH, DINNER]


def test_filter_by_category_no_match():
    assert tracker.filter_by_category(EXPENSES, "rent") == []


# Requirement 6: monthly_totals

def test_monthly_totals():
    assert tracker.monthly_totals(EXPENSES) == {"2026-01": 14.9, "2026-02": 30.0}


def test_monthly_totals_empty():
    assert tracker.monthly_totals([]) == {}


# Requirement 7: category_summary

def test_category_summary():
    assert tracker.category_summary(EXPENSES) == {"food": (2, 42.5), "transport": (1, 2.4)}


def test_category_summary_empty():
    assert tracker.category_summary([]) == {}


# Requirement 8: format_expense

def test_format_expense_contains_all_parts():
    line = tracker.format_expense(LUNCH)
    assert "2026-01-05" in line and "food" in line and "12.50" in line and "lunch" in line
    assert "\n" not in line


# Requirement 9: save_expenses and load_expenses

def test_save_then_load_round_trip(tmp_path):
    path = tmp_path / "expenses.json"
    tracker.save_expenses(path, EXPENSES)
    assert json.loads(path.read_text()) == EXPENSES
    assert tracker.load_expenses(path) == EXPENSES


def test_load_missing_file_gives_empty_list(tmp_path):
    assert tracker.load_expenses(tmp_path / "missing.json") == []


def test_load_corrupt_file_raises(tmp_path):
    path = tmp_path / "expenses.json"
    path.write_text("{not json")
    with pytest.raises(tracker.DataFileError):
        tracker.load_expenses(path)


def test_load_wrong_shape_raises(tmp_path):
    path = tmp_path / "expenses.json"
    path.write_text('{"date": "2026-01-01"}')
    with pytest.raises(tracker.DataFileError):
        tracker.load_expenses(path)
    path.write_text('[{"date": "2026-01-01"}]')
    with pytest.raises(tracker.DataFileError):
        tracker.load_expenses(path)


# Requirement 10: the menu loop

def feed_input(monkeypatch, answers):
    """Make input() return each answer in turn, as if the user typed them."""
    answers = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))


def test_main_adds_and_saves_an_expense(tmp_path, monkeypatch, capsys):
    path = tmp_path / "expenses.json"
    feed_input(monkeypatch, ["1", "2026-01-05", "Food", "12.50", "lunch", "6"])
    tracker.main(path)
    assert tracker.load_expenses(path) == [LUNCH]
    assert "Goodbye" in capsys.readouterr().out


def test_main_reasks_after_invalid_expense(tmp_path, monkeypatch):
    path = tmp_path / "expenses.json"
    feed_input(monkeypatch, [
        "1", "not-a-date", "food", "5", "",       # rejected
        "2026-01-05", "food", "12.5", "lunch",    # accepted
        "6",
    ])
    tracker.main(path)
    assert tracker.load_expenses(path) == [LUNCH]


def test_main_reports_monthly_totals(tmp_path, monkeypatch, capsys):
    path = tmp_path / "expenses.json"
    tracker.save_expenses(path, EXPENSES)
    feed_input(monkeypatch, ["4", "6"])
    tracker.main(path)
    output = capsys.readouterr().out
    assert "2026-01" in output and "14.90" in output and "30.00" in output


def test_main_survives_corrupt_file(tmp_path, monkeypatch, capsys):
    path = tmp_path / "expenses.json"
    path.write_text("{not json")
    feed_input(monkeypatch, ["2", "6"])
    tracker.main(path)
    output = capsys.readouterr().out
    assert "No expenses" in output
    assert (tmp_path / "expenses.bak").exists()


def test_main_rejects_unknown_option(tmp_path, monkeypatch, capsys):
    feed_input(monkeypatch, ["9", "6"])
    tracker.main(tmp_path / "expenses.json")
    assert "1 to 6" in capsys.readouterr().out

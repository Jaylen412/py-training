"""Expense tracker: a command-line program that records expenses in a JSON file.

Run it from the repository root with:
    python part-1-python-fundamentals/project/starter/expense_tracker.py

Each expense is a dictionary with four keys:
    {"date": "2026-01-05", "category": "food", "amount": 12.5, "note": "lunch"}

Replace every `raise NotImplementedError`. The numbers in the docstrings
match the requirements in the project README and the sections of
test_project_1.py.
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"

MENU = """
1. Add an expense
2. List all expenses
3. Filter by category
4. Monthly totals
5. Category summary
6. Quit"""


class DataFileError(Exception):
    """Raised when the data file exists but cannot be read as expenses."""


# ---------- Validation ----------

def validate_date(text):
    """Requirement 1. Strip spaces, then return the date if it has the form
    YYYY-MM-DD: four digits, a dash, two digits, a dash, two digits, with
    month 01-12 and day 01-31. Otherwise raise ValueError.

    Example: validate_date(" 2026-01-05 ") returns "2026-01-05"
    """
    raise NotImplementedError


def parse_amount(text):
    """Requirement 2. Convert `text` to a float rounded to 2 decimal places.
    Raise ValueError if it is not a number or is not positive.

    Example: parse_amount("3.456") returns 3.46
    """
    raise NotImplementedError


def make_expense(date, category, amount, note=""):
    """Requirement 3. Return an expense dictionary built from text input.
    The date and amount are checked with the functions above, the category
    is stripped and lower-cased (and must not be empty), the note stripped.

    Example: make_expense("2026-01-05", " Food ", "12.50", "lunch") returns
    {"date": "2026-01-05", "category": "food", "amount": 12.5, "note": "lunch"}
    """
    raise NotImplementedError


# ---------- Working with a list of expenses ----------

def add_expense(expenses, expense):
    """Requirement 4. Return a NEW list with `expense` added at the end.
    Do not change `expenses`.
    """
    raise NotImplementedError


def filter_by_category(expenses, category):
    """Requirement 5. Return the expenses in `category`, ignoring case and
    surrounding spaces in the argument.
    """
    raise NotImplementedError


def monthly_totals(expenses):
    """Requirement 6. Return a dictionary mapping each month ("YYYY-MM",
    the first 7 characters of the date) to the total spent, rounded to 2
    decimal places.

    Example: {"2026-01": 14.9, "2026-02": 30.0}
    """
    raise NotImplementedError


def category_summary(expenses):
    """Requirement 7. Return a dictionary mapping each category to a tuple
    (number of expenses, total amount rounded to 2 decimal places).

    Example: {"food": (2, 42.5), "transport": (1, 2.4)}
    """
    raise NotImplementedError


def format_expense(expense):
    """Requirement 8. Return the expense as one line of text containing the
    date, category, amount with 2 decimal places, and note.

    Example: "2026-01-05  food             12.50  lunch"
    """
    raise NotImplementedError


# ---------- Files ----------

def save_expenses(path, expenses):
    """Requirement 9. Save the list of expenses to `path` as JSON."""
    raise NotImplementedError


def load_expenses(path):
    """Requirement 9. Return the list of expenses stored at `path`.
    - If the file does not exist, return [].
    - If it is not valid JSON, raise DataFileError.
    - If it is not a list, or any item is not a dictionary with all four
      keys, raise DataFileError.
    """
    raise NotImplementedError


# ---------- The interactive program ----------

def main(path=DATA_FILE):
    """Requirement 10. Run the menu loop until the user chooses 6.

    - Load the expenses at the start. If the file is corrupt, rename it to
      have the suffix .bak (path.rename(path.with_suffix(".bak"))), print a
      warning, and start with an empty list.
    - Print MENU and ask for a choice with input().
    - 1: ask for date, category, amount and note (in that order); if
      make_expense raises ValueError, print the problem and ask for all four
      again. Then add it and save the file straight away.
    - 2: print every expense with format_expense, or "No expenses." if none.
    - 3: ask for a category and print the matching expenses the same way.
    - 4: print each month and its total (2 decimal places), in month order.
    - 5: print each category, its count and its total, in category order.
    - 6: print "Goodbye!" and stop.
    - Anything else: print "Please choose a number from 1 to 6."
    """
    raise NotImplementedError


# This runs main() only when the file is run directly, not when the tests
# import it. You will learn how it works in lesson 08-01.
if __name__ == "__main__":
    main()

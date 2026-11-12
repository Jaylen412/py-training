"""Expense tracker: a command-line program that records expenses in a JSON file.

Run it from the repository root with:
    python part-1-python-fundamentals/project/solution/expense_tracker.py
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


# ---------- Validation (requirements 1 to 3) ----------

def validate_date(text):
    """Return the date as "YYYY-MM-DD" if valid, otherwise raise ValueError."""
    text = text.strip()
    parts = text.split("-")
    if len(parts) != 3 or len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        raise ValueError(f"date must look like YYYY-MM-DD, got {text!r}")
    if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        raise ValueError(f"date must contain only digits and dashes, got {text!r}")
    month = int(parts[1])
    day = int(parts[2])
    if not 1 <= month <= 12:
        raise ValueError(f"month must be 01 to 12, got {parts[1]}")
    if not 1 <= day <= 31:
        raise ValueError(f"day must be 01 to 31, got {parts[2]}")
    return text


def parse_amount(text):
    """Return a positive amount rounded to 2 decimal places, or raise ValueError."""
    try:
        amount = float(text)
    except ValueError:
        raise ValueError(f"amount must be a number, got {text!r}")
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    return round(amount, 2)


def make_expense(date, category, amount, note=""):
    """Validate the parts of an expense and return it as a dictionary."""
    category = category.strip().lower()
    if not category:
        raise ValueError("category must not be empty")
    return {
        "date": validate_date(date),
        "category": category,
        "amount": parse_amount(amount),
        "note": note.strip(),
    }


# ---------- Working with a list of expenses (requirements 4 to 7) ----------

def add_expense(expenses, expense):
    """Return a new list with `expense` added at the end."""
    return expenses + [expense]


def filter_by_category(expenses, category):
    """Return the expenses whose category matches, ignoring case and spaces."""
    wanted = category.strip().lower()
    return [expense for expense in expenses if expense["category"] == wanted]


def monthly_totals(expenses):
    """Return a dictionary mapping "YYYY-MM" to the total spent that month."""
    totals = {}
    for expense in expenses:
        month = expense["date"][:7]
        totals[month] = totals.get(month, 0) + expense["amount"]
    return {month: round(total, 2) for month, total in totals.items()}


def category_summary(expenses):
    """Return a dictionary mapping category to (number of expenses, total)."""
    counts = {}
    totals = {}
    for expense in expenses:
        category = expense["category"]
        counts[category] = counts.get(category, 0) + 1
        totals[category] = totals.get(category, 0) + expense["amount"]
    return {category: (counts[category], round(totals[category], 2)) for category in counts}


def format_expense(expense):
    """Return one expense as a single aligned line of text."""
    return f"{expense['date']}  {expense['category']:<12}{expense['amount']:>10.2f}  {expense['note']}"


# ---------- Files (requirements 8 and 9) ----------

def save_expenses(path, expenses):
    """Save the list of expenses to `path` as JSON."""
    with open(path, "w") as file:
        json.dump(expenses, file, indent=2)


def load_expenses(path):
    """Return the expenses stored at `path`.

    A missing file means no expenses yet. A file that is not valid JSON,
    or does not hold a list of expenses, raises DataFileError.
    """
    try:
        with open(path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise DataFileError(f"{path} is not valid JSON")
    if not isinstance(data, list):
        raise DataFileError(f"{path} does not contain a list of expenses")
    for item in data:
        if not isinstance(item, dict) or not {"date", "category", "amount", "note"} <= set(item):
            raise DataFileError(f"{path} contains a malformed expense: {item!r}")
    return data


# ---------- The interactive program (requirement 10) ----------

def print_expenses(expenses):
    """Print expenses one per line, or a message if there are none."""
    if not expenses:
        print("No expenses.")
        return
    for expense in expenses:
        print(format_expense(expense))


def ask_for_expense():
    """Ask for the parts of an expense until they are valid, and return it."""
    while True:
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ")
        amount = input("Amount: ")
        note = input("Note (optional): ")
        try:
            return make_expense(date, category, amount, note)
        except ValueError as error:
            print(f"Invalid expense: {error}. Please try again.")


def start_expenses(path):
    """Load expenses, starting fresh (with a backup) if the file is corrupt."""
    try:
        return load_expenses(path)
    except DataFileError as error:
        backup = path.with_suffix(".bak")
        path.rename(backup)
        print(f"Warning: {error}. Moved it to {backup.name} and started a new file.")
        return []


def main(path=DATA_FILE):
    """Run the menu loop until the user chooses Quit."""
    expenses = start_expenses(path)
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            expenses = add_expense(expenses, ask_for_expense())
            save_expenses(path, expenses)
            print("Saved.")
        elif choice == "2":
            print_expenses(expenses)
        elif choice == "3":
            category = input("Category: ")
            print_expenses(filter_by_category(expenses, category))
        elif choice == "4":
            totals = monthly_totals(expenses)
            for month in sorted(totals):
                print(f"{month}  {totals[month]:>10.2f}")
            if not totals:
                print("No expenses.")
        elif choice == "5":
            summary = category_summary(expenses)
            for category in sorted(summary):
                count, total = summary[category]
                print(f"{category:<12}{count:>4} items {total:>10.2f}")
            if not summary:
                print("No expenses.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()

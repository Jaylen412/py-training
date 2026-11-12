# Part 1 Project: Expense Tracker

## Brief

Build a command-line program that keeps track of your spending. You type in expenses (a date, a category, an amount and a note), and the program saves them to a JSON file so they are still there next time. It can list them, filter them by category, total them by month, and summarise them by category. It must not crash on bad input or on a missing or damaged data file.

This project uses everything from Part 1: variables, strings, conditionals, loops, functions, lists, dictionaries, files, JSON and exceptions.

```
1. Add an expense
2. List all expenses
3. Filter by category
4. Monthly totals
5. Category summary
6. Quit
Choose an option: 1
Date (YYYY-MM-DD): 2026-01-05
Category: Food
Amount: 12.50
Note (optional): lunch
Saved.
```

## Getting started

Work in `starter/expense_tracker.py`. Every function is already named, with a docstring saying exactly what it must do. Run the tests as you go:

```
python -m pytest part-1-python-fundamentals/project/starter
```

Run the program itself with:

```
python part-1-python-fundamentals/project/starter/expense_tracker.py
```

It stores its data in `starter/expenses.json`, which is created the first time you add an expense.

## Requirements

1. `validate_date` accepts dates in the form `YYYY-MM-DD` (month 01 to 12, day 01 to 31) and raises `ValueError` for anything else.
2. `parse_amount` turns text into a positive amount rounded to 2 decimal places, raising `ValueError` otherwise.
3. `make_expense` builds a validated expense dictionary, with the category stripped and lower-cased.
4. `add_expense` returns a new list with the expense added, without changing the original.
5. `filter_by_category` returns the expenses in one category, ignoring case.
6. `monthly_totals` returns the total spent in each month.
7. `category_summary` returns the number of expenses and the total for each category.
8. `format_expense` turns one expense into a single readable line.
9. `save_expenses` and `load_expenses` store the list as JSON. A missing file means "no expenses yet"; a damaged file raises `DataFileError`.
10. `main` runs the menu loop described in its docstring: it re-asks after invalid input, saves after every addition, and moves a damaged file aside to `expenses.bak` instead of crashing.

## Suggested order of work

1. Requirements 1 and 2: the validators. Get their tests passing first; everything else builds on them.
2. Requirement 3, which calls them.
3. Requirements 4 to 8: the pure functions that work on a list of expenses. Use the sample data at the top of the test file to work examples by hand first (07-01).
4. Requirement 9: saving and loading. Test it by saving a list and loading it back.
5. Requirement 10: the menu. Write option 6 (quit) first, then 2, then 1, and so on, running the program after each one.

Each of these steps should only take a few lines of code if you use the functions you have already written.

## Stretch goals

1. Add a menu option to delete an expense, chosen by its number in the list (show numbers with `enumerate`).
2. Add a monthly budget per category, stored in a second JSON file, and warn when a month's spending in a category goes over it.
3. Make `validate_date` reject impossible dates such as `2026-02-30` and `2026-04-31`, including leap years (reuse your `is_leap_year` from 03-02).

## Reference solution

`solution/expense_tracker.py` passes every test. Try to finish the project yourself before reading it. To run the tests against it:

```
COURSE_SOLUTIONS=1 python -m pytest part-1-python-fundamentals/project/starter
```

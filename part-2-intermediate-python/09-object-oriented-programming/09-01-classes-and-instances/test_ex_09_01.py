import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_09_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_09_01"
)


def test_rectangle_attributes_and_area():
    rectangle = mod.Rectangle(3, 4)
    assert (rectangle.width, rectangle.height) == (3, 4)
    assert rectangle.area() == 12


def test_rectangle_perimeter():
    assert mod.Rectangle(3, 4).perimeter() == 14
    assert mod.Rectangle(0, 0).perimeter() == 0


def test_rectangle_scale_changes_the_instance():
    rectangle = mod.Rectangle(3, 4)
    assert rectangle.scale(2) is None
    assert (rectangle.width, rectangle.height) == (6, 8)
    assert rectangle.area() == 48


def test_rectangles_are_independent():
    first = mod.Rectangle(1, 1)
    second = mod.Rectangle(1, 1)
    first.scale(10)
    assert second.area() == 1


def test_tally_counter_clicks():
    counter = mod.TallyCounter()
    assert counter.count == 0
    assert counter.click() == 1
    assert counter.click(3) == 4


def test_tally_counter_reset_keeps_highest():
    counter = mod.TallyCounter()
    counter.click(5)
    counter.reset()
    assert counter.count == 0
    assert counter.highest == 5
    counter.click(2)
    assert counter.highest == 5


def test_bank_account_deposit_and_withdraw():
    account = mod.BankAccount("Ada", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120
    assert account.transactions == 2
    assert account.describe() == "Ada: 120.00"


def test_bank_account_default_balance():
    assert mod.BankAccount("Alan").describe() == "Alan: 0.00"


def test_bank_account_rejects_bad_amounts():
    account = mod.BankAccount("Ada", 10)
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.withdraw(-5)
    with pytest.raises(ValueError):
        account.withdraw(11)


def test_bank_account_failed_withdrawal_changes_nothing():
    account = mod.BankAccount("Ada", 10)
    with pytest.raises(ValueError):
        account.withdraw(50)
    assert account.balance == 10
    assert account.transactions == 0

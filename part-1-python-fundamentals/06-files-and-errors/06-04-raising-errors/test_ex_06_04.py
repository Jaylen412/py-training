import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_06_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_06_04"
)

# pytest.raises checks that the code inside the `with` block raises the
# given exception. The test fails if it does not.


def test_validate_age_valid():
    assert mod.validate_age(30) == 30
    assert mod.validate_age(0) == 0
    assert mod.validate_age(150) == 150


def test_validate_age_out_of_range():
    with pytest.raises(ValueError):
        mod.validate_age(-1)
    with pytest.raises(ValueError):
        mod.validate_age(151)


def test_validate_age_wrong_type():
    with pytest.raises(TypeError):
        mod.validate_age("30")
    with pytest.raises(TypeError):
        mod.validate_age(30.5)


def test_parse_quantity():
    assert mod.parse_quantity(" 3 ") == 3


def test_parse_quantity_not_whole_number():
    with pytest.raises(ValueError):
        mod.parse_quantity("2.5")
    with pytest.raises(ValueError, match="abc"):
        mod.parse_quantity("abc")


def test_parse_quantity_not_positive():
    with pytest.raises(ValueError):
        mod.parse_quantity("0")
    with pytest.raises(ValueError):
        mod.parse_quantity("-4")


def test_withdraw():
    assert mod.withdraw(100, 30) == 70
    assert mod.withdraw(100, 100) == 0


def test_withdraw_too_much():
    with pytest.raises(mod.InsufficientFundsError):
        mod.withdraw(100, 300)


def test_withdraw_bad_amount():
    with pytest.raises(ValueError):
        mod.withdraw(100, 0)
    with pytest.raises(ValueError):
        mod.withdraw(100, -5)


def test_require_fields_all_present():
    assert mod.require_fields({"name": "Ada", "email": "a@b.c"}, ["name", "email"]) is None


def test_require_fields_missing():
    with pytest.raises(KeyError, match="age, email"):
        mod.require_fields({"name": "Ada"}, ["name", "email", "age"])


def test_require_fields_empty_requirements():
    assert mod.require_fields({}, []) is None

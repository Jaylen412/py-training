import importlib
import os

mod = importlib.import_module(
    "sol_03_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_03_01"
)


def test_sign_of_positive():
    assert mod.sign_of(5) == "positive"


def test_sign_of_negative():
    assert mod.sign_of(-3) == "negative"


def test_sign_of_zero():
    assert mod.sign_of(0) == "zero"


def test_letter_grade_middle_of_bands():
    assert mod.letter_grade(95) == "A"
    assert mod.letter_grade(72) == "B"
    assert mod.letter_grade(60) == "C"
    assert mod.letter_grade(10) == "F"


def test_letter_grade_boundaries():
    assert mod.letter_grade(90) == "A"
    assert mod.letter_grade(89) == "B"
    assert mod.letter_grade(70) == "B"
    assert mod.letter_grade(50) == "C"
    assert mod.letter_grade(49) == "F"


def test_ticket_price_each_band():
    assert mod.ticket_price(1) == 0
    assert mod.ticket_price(10) == 6
    assert mod.ticket_price(30) == 10
    assert mod.ticket_price(80) == 7


def test_ticket_price_boundaries():
    assert mod.ticket_price(3) == 6
    assert mod.ticket_price(15) == 6
    assert mod.ticket_price(16) == 10
    assert mod.ticket_price(64) == 10
    assert mod.ticket_price(65) == 7


def test_larger_of():
    assert mod.larger_of(3, 8) == 8
    assert mod.larger_of(8, 3) == 8


def test_larger_of_equal_and_negative():
    assert mod.larger_of(4, 4) == 4
    assert mod.larger_of(-1, -7) == -1


def test_describe_temperature():
    assert mod.describe_temperature(-5) == "freezing"
    assert mod.describe_temperature(5) == "cold"
    assert mod.describe_temperature(15) == "mild"
    assert mod.describe_temperature(25) == "warm"
    assert mod.describe_temperature(35) == "hot"


def test_describe_temperature_boundaries():
    assert mod.describe_temperature(0) == "cold"
    assert mod.describe_temperature(10) == "mild"
    assert mod.describe_temperature(30) == "hot"

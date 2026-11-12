import importlib
import os

mod = importlib.import_module(
    "sol_02_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_02_03"
)


def test_first_and_last():
    assert mod.first_and_last("Python") == "Pn"


def test_first_and_last_single_character():
    assert mod.first_and_last("a") == "aa"


def test_initials():
    assert mod.initials("Ada", "Lovelace") == "A.L."


def test_initials_keeps_case():
    assert mod.initials("grace", "Hopper") == "g.H."


def test_reverse_text():
    assert mod.reverse_text("stressed") == "desserts"


def test_reverse_text_empty():
    assert mod.reverse_text("") == ""


def test_reverse_text_palindrome():
    assert mod.reverse_text("racecar") == "racecar"


def test_without_ends():
    assert mod.without_ends("[hello]") == "hello"


def test_without_ends_two_characters():
    assert mod.without_ends("ab") == ""


def test_make_tag():
    assert mod.make_tag("div") == "<div>"


def test_make_tag_empty_name():
    assert mod.make_tag("") == "<>"

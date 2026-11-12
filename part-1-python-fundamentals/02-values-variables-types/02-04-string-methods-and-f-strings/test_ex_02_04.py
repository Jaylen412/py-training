import importlib
import os

mod = importlib.import_module(
    "sol_02_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_02_04"
)


def test_clean_name():
    assert mod.clean_name("  ada LOVELACE ") == "Ada Lovelace"


def test_clean_name_already_clean():
    assert mod.clean_name("Grace Hopper") == "Grace Hopper"


def test_count_words():
    assert mod.count_words("the quick  brown fox") == 4


def test_count_words_empty():
    assert mod.count_words("") == 0


def test_count_words_only_spaces():
    assert mod.count_words("    ") == 0


def test_slugify():
    assert mod.slugify(" Intro To Python ") == "intro-to-python"


def test_slugify_single_word():
    assert mod.slugify("Python") == "python"


def test_format_price():
    assert mod.format_price(1234.5) == "$1,234.50"


def test_format_price_small():
    assert mod.format_price(0.5) == "$0.50"


def test_format_price_rounds():
    assert mod.format_price(1000000) == "$1,000,000.00"


def test_format_percentage():
    assert mod.format_percentage(0.4567) == "45.7%"


def test_format_percentage_whole():
    assert mod.format_percentage(1) == "100.0%"


def test_is_mentioned():
    assert mod.is_mentioned("I love Python", "python") is True


def test_is_mentioned_missing():
    assert mod.is_mentioned("I love Python", "java") is False


def test_is_mentioned_upper_case_word():
    assert mod.is_mentioned("data science", "SCIENCE") is True

import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_10_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_10_03"
)


def test_product():
    assert mod.product(2, 3, 4) == 24
    assert mod.product(*[1.5, 2]) == pytest.approx(3.0)


def test_product_no_arguments():
    assert mod.product() == 1


def test_make_tag():
    result = mod.make_tag("a", "Click", " here", href="/home", id="link")
    assert result == '<a href="/home" id="link">Click here</a>'


def test_make_tag_empty():
    assert mod.make_tag("br") == "<br></br>"
    assert mod.make_tag("p", "hi") == "<p>hi</p>"


def test_merge_settings():
    result = mod.merge_settings({"a": 1, "b": 2}, {"b": 3}, {"c": 4})
    assert result == {"a": 1, "b": 3, "c": 4}


def test_merge_settings_leaves_arguments_alone():
    first = {"a": 1}
    result = mod.merge_settings(first, {"a": 2})
    assert first == {"a": 1}
    assert result == {"a": 2}
    assert mod.merge_settings() == {}


def test_call_with_defaults():
    assert mod.call_with_defaults(dict) == {"verbose": False, "retries": 3}
    assert mod.call_with_defaults(dict, retries=5) == {"verbose": False, "retries": 5}


def test_call_with_defaults_passes_positional_and_extra_keywords():
    def collect(*args, **kwargs):
        return args, kwargs

    args, kwargs = mod.call_with_defaults(collect, 1, 2, verbose=True, colour="red")
    assert args == (1, 2)
    assert kwargs == {"verbose": True, "retries": 3, "colour": "red"}


def test_format_money():
    assert mod.format_money(1234.5) == "$1,234.50"
    assert mod.format_money(1234.5, currency="EUR ", decimals=0) == "EUR 1,234"


def test_format_money_options_are_keyword_only():
    with pytest.raises(TypeError):
        mod.format_money(10, "EUR ")

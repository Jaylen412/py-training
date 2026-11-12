import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_08_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_08_04"
)


def test_parse_key_values():
    assert mod.parse_key_values(["name=Ada", "age=36"]) == {"name": "Ada", "age": "36"}


def test_parse_key_values_splits_on_first_equals():
    assert mod.parse_key_values(["eq=a=b", "empty="]) == {"eq": "a=b", "empty": ""}
    assert mod.parse_key_values([]) == {}


def test_parse_key_values_rejects_missing_equals():
    with pytest.raises(ValueError):
        mod.parse_key_values(["name"])


def test_convert():
    assert mod.convert(100, "f") == pytest.approx(212.0)
    assert mod.convert(212, "c") == pytest.approx(100.0)


def test_convert_minus_forty():
    assert mod.convert(-40, "f") == pytest.approx(-40.0)
    assert mod.convert(-40, "c") == pytest.approx(-40.0)


def test_build_parser_defaults():
    args = mod.build_parser().parse_args(["100"])
    assert args.value == 100.0
    assert args.to == "f"
    assert args.decimals == 1


def test_build_parser_options():
    args = mod.build_parser().parse_args(["--to", "c", "50", "--decimals", "3"])
    assert (args.value, args.to, args.decimals) == (50.0, "c", 3)


def test_build_parser_rejects_bad_unit():
    with pytest.raises(SystemExit):
        mod.build_parser().parse_args(["100", "--to", "k"])


def test_main_default(capsys):
    assert mod.main(["100"]) == 0
    assert capsys.readouterr().out == "212.0 F\n"


def test_main_to_celsius_no_decimals(capsys):
    assert mod.main(["212", "--to", "c", "--decimals", "0"]) == 0
    assert capsys.readouterr().out == "100 C\n"


def test_main_below_absolute_zero(capsys):
    assert mod.main(["-300"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "absolute zero" in captured.err

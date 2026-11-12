import importlib
import os

mod = importlib.import_module(
    "sol_01_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_01_02"
)


# capsys is a pytest tool that captures everything a function prints.

def test_print_greeting(capsys):
    mod.print_greeting()
    assert capsys.readouterr().out == "Hello, world!\n"


def test_print_greeting_prints_one_line_only(capsys):
    mod.print_greeting()
    assert capsys.readouterr().out.count("\n") == 1


def test_print_name_card(capsys):
    mod.print_name_card()
    assert capsys.readouterr().out == "Name: Ada\nLanguage: Python\nLevel: Beginner\n"


def test_print_name_card_has_no_blank_lines(capsys):
    mod.print_name_card()
    lines = capsys.readouterr().out.split("\n")
    assert "" not in lines[:-1]


def test_print_date(capsys):
    mod.print_date()
    assert capsys.readouterr().out == "2026/01/31\n"


def test_print_date_has_no_spaces(capsys):
    mod.print_date()
    assert " " not in capsys.readouterr().out


def test_print_progress(capsys):
    mod.print_progress()
    assert capsys.readouterr().out == "Loading...done\n"


def test_print_progress_is_one_line(capsys):
    mod.print_progress()
    assert capsys.readouterr().out.count("\n") == 1


def test_print_box(capsys):
    mod.print_box()
    assert capsys.readouterr().out == "+-----+\n|  Hi |\n+-----+\n"


def test_print_box_lines_are_equal_width(capsys):
    mod.print_box()
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 3
    assert len(lines[0]) == len(lines[1]) == len(lines[2]) == 7

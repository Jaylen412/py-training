import importlib
import os

mod = importlib.import_module(
    "sol_06_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_06_01"
)

# tmp_path is a pytest tool: a fresh, empty temporary folder for each test.


def test_count_lines(tmp_path):
    path = tmp_path / "three.txt"
    path.write_text("a\nb\nc\n")
    assert mod.count_lines(path) == 3


def test_count_lines_empty_and_no_final_newline(tmp_path):
    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert mod.count_lines(empty) == 0
    unfinished = tmp_path / "unfinished.txt"
    unfinished.write_text("a\nb")
    assert mod.count_lines(unfinished) == 2


def test_write_lines(tmp_path):
    path = tmp_path / "out.txt"
    mod.write_lines(path, ["a", "b"])
    assert path.read_text() == "a\nb\n"


def test_write_lines_replaces_and_handles_empty(tmp_path):
    path = tmp_path / "out.txt"
    path.write_text("old content\n")
    mod.write_lines(path, [])
    assert path.read_text() == ""


def test_append_line(tmp_path):
    path = tmp_path / "log.txt"
    path.write_text("a\n")
    mod.append_line(path, "b")
    assert path.read_text() == "a\nb\n"


def test_append_line_creates_file(tmp_path):
    path = tmp_path / "new.txt"
    mod.append_line(path, "first")
    assert path.read_text() == "first\n"


def test_longest_line(tmp_path):
    path = tmp_path / "words.txt"
    path.write_text("hi\nhello\nhey\n")
    assert mod.longest_line(path) == "hello"


def test_longest_line_tie_and_empty(tmp_path):
    tie = tmp_path / "tie.txt"
    tie.write_text("abc\nxyz\n")
    assert mod.longest_line(tie) == "abc"
    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert mod.longest_line(empty) == ""


def test_file_stats(tmp_path):
    path = tmp_path / "cat.txt"
    path.write_text("the cat\nsat\n")
    assert mod.file_stats(path) == (2, 3, 12)


def test_file_stats_empty(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("")
    assert mod.file_stats(path) == (0, 0, 0)

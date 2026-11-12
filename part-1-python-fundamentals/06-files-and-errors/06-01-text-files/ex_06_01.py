"""Exercises for 06-01 Reading and writing text files.

Each `path` argument is a pathlib.Path. Use `with open(...)` or the Path
read_text/write_text shortcuts.
"""


def count_lines(path):
    """Return the number of lines in the file.

    Example: for a file containing "a\\nb\\nc\\n", returns 3
    """
    raise NotImplementedError


def write_lines(path, lines):
    """Write each string in `lines` to the file on its own line,
    replacing anything already there. Every line, including the last,
    ends with "\\n". An empty list produces an empty file.

    Example: write_lines(path, ["a", "b"]) leaves the file containing "a\\nb\\n"
    """
    raise NotImplementedError


def append_line(path, line):
    """Add `line` followed by "\\n" to the end of the file, keeping what is
    already there. Create the file if it does not exist.

    Example: if the file contains "a\\n", append_line(path, "b") makes it "a\\nb\\n"
    """
    raise NotImplementedError


def longest_line(path):
    """Return the longest line in the file, without its newline.
    If several are equally long, return the first. Return "" for an
    empty file.

    Example: for a file containing "hi\\nhello\\nhey\\n", returns "hello"
    """
    raise NotImplementedError


def file_stats(path):
    """Return a tuple (lines, words, characters) for the file.
    Characters includes the newline characters. Words are separated
    by whitespace.

    Example: for a file containing "the cat\\nsat\\n", returns (2, 3, 12)
    """
    raise NotImplementedError

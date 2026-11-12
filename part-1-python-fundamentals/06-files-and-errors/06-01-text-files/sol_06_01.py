"""Solutions for 06-01 Reading and writing text files."""


def count_lines(path):
    """Return the number of lines in the file."""
    count = 0
    with open(path) as file:
        for _ in file:
            count += 1
    return count


def write_lines(path, lines):
    """Write each string in `lines` to the file on its own line."""
    with open(path, "w") as file:
        for line in lines:
            file.write(line + "\n")


def append_line(path, line):
    """Add `line` to the end of the file."""
    with open(path, "a") as file:
        file.write(line + "\n")


def longest_line(path):
    """Return the longest line in the file, without its newline."""
    longest = ""
    with open(path) as file:
        for line in file:
            line = line.rstrip("\n")
            if len(line) > len(longest):
                longest = line
    return longest


def file_stats(path):
    """Return (lines, words, characters) for the file."""
    content = path.read_text()
    return len(content.splitlines()), len(content.split()), len(content)

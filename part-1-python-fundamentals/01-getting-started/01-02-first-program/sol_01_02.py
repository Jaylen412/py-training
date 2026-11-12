"""Solutions for 01-02 Your first program."""


def print_greeting():
    """Print the text Hello, world!"""
    print("Hello, world!")


def print_name_card():
    """Print a three-line name card."""
    print("Name: Ada")
    print("Language: Python")
    print("Level: Beginner")


def print_date():
    """Print 2026/01/31 using sep."""
    print("2026", "01", "31", sep="/")


def print_progress():
    """Print Loading...done using two print calls."""
    # end replaces the usual new line, so "done" lands on the same line.
    print("Loading", end="...")
    print("done")


def print_box():
    """Print a small box."""
    print("+-----+")
    print("|  Hi |")
    print("+-----+")

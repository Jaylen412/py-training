"""Exercises for 08-04 Command-line programs.

A small temperature conversion tool, used like:
    python convert.py 100 --to f --decimals 0
"""
import argparse
import sys

ABSOLUTE_ZERO_C = -273.15


def parse_key_values(arguments):
    """Turn a list of "key=value" strings into a dictionary of strings.
    Split on the FIRST "=" only. Raise ValueError if an item has no "=".

    Example: parse_key_values(["name=Ada", "eq=a=b"]) returns {"name": "Ada", "eq": "a=b"}
    """
    raise NotImplementedError


def convert(value, to):
    """Convert a temperature. If `to` is "f", `value` is in Celsius and the
    result is Fahrenheit. If `to` is "c", `value` is in Fahrenheit and the
    result is Celsius.

    Example: convert(100, "f") returns 212.0
    """
    raise NotImplementedError


def build_parser():
    """Return an argparse.ArgumentParser with:
    - a positional argument "value" with type=float,
    - an option "--to" with choices=["c", "f"] and default "f",
    - an option "--decimals" with type=int and default 1.

    Example: build_parser().parse_args(["100"]).to returns "f"
    """
    raise NotImplementedError


def main(argv):
    """Parse `argv` with build_parser(). Work out the input temperature in
    Celsius (the value itself if converting to "f", otherwise convert it to
    Celsius first). If that is below ABSOLUTE_ZERO_C, print an error to
    sys.stderr and return 1. Otherwise print the converted value rounded to
    `decimals` places, a space, and the upper-case unit, then return 0.

    Example: main(["100"]) prints "212.0 F" and returns 0
    Example: main(["212", "--to", "c", "--decimals", "0"]) prints "100 C"
    """
    raise NotImplementedError

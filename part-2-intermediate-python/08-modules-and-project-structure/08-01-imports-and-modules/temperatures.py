"""Helper module for lesson 08-01: temperature conversions."""

FREEZING_C = 0.0


def c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


print(f"temperatures.py is running, and its __name__ is {__name__!r}")

if __name__ == "__main__":
    # Only runs when this file is run directly, not when it is imported.
    print("Self-test:", c_to_f(100), f_to_c(212))

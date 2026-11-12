"""Solutions for 04-01 Defining and calling functions."""


def square(number):
    """Return `number` multiplied by itself."""
    return number * number


def make_greeting(name):
    """Return a greeting for `name`."""
    return f"Hello, {name}!"


def is_even(number):
    """Return True if `number` is even."""
    return number % 2 == 0


def bmi(weight_kg, height_m):
    """Return body mass index rounded to one decimal place."""
    return round(weight_kg / height_m ** 2, 1)


def format_duration(seconds):
    """Turn seconds into a string such as "1h 2m 3s"."""
    hours = seconds // 3600
    minutes = seconds % 3600 // 60   # what is left after the hours, in minutes
    remaining_seconds = seconds % 60
    return f"{hours}h {minutes}m {remaining_seconds}s"

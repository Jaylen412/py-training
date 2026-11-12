"""Solutions for 03-01 Conditionals."""


def sign_of(number):
    """Return "positive", "negative" or "zero" depending on `number`."""
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def letter_grade(score):
    """Return a letter grade for a score from 0 to 100."""
    # Highest threshold first, because the first true branch wins.
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"


def ticket_price(age):
    """Return the price of a cinema ticket for someone of `age`."""
    if age < 3:
        return 0
    elif age < 16:
        return 6
    elif age < 65:
        return 10
    else:
        return 7


def larger_of(first, second):
    """Return the larger of two numbers."""
    return first if first >= second else second


def describe_temperature(celsius):
    """Return a word for a temperature in Celsius."""
    if celsius < 0:
        return "freezing"
    elif celsius < 10:
        return "cold"
    elif celsius < 20:
        return "mild"
    elif celsius < 30:
        return "warm"
    else:
        return "hot"

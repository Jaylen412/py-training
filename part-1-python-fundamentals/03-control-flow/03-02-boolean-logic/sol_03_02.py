"""Solutions for 03-02 Boolean logic."""


def is_leap_year(year):
    """Return True if `year` is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def can_ride(height_cm, age):
    """Return True if someone may go on the ride."""
    return height_cm >= 120 or (age >= 10 and height_cm >= 110)


def is_weekend(day):
    """Return True if `day` is Saturday or Sunday, ignoring case."""
    day = day.lower()
    return day == "saturday" or day == "sunday"


def in_range(value, low, high):
    """Return True if `value` is between `low` and `high`, inclusive."""
    return low <= value <= high


def is_valid_username(username):
    """Return True if the username follows all three rules."""
    # The length check comes first so that username[0] is never
    # looked at for an empty string (short-circuiting).
    return (
        3 <= len(username) <= 12
        and " " not in username
        and username[0] not in "0123456789"
    )

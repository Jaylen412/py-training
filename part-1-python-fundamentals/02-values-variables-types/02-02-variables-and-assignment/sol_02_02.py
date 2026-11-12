"""Solutions for 02-02 Variables and assignment."""


def area_of_room(length, width):
    """Return the floor area of a rectangular room."""
    area = length * width
    return area


def price_after_discount(price, discount_percent):
    """Return the price after taking `discount_percent` per cent off."""
    discount_amount = price * discount_percent / 100
    discounted_price = price - discount_amount
    return discounted_price


def final_balance(start, deposit, withdrawal, interest_rate):
    """Apply a deposit, a withdrawal and one year of interest."""
    balance = start
    balance += deposit
    balance -= withdrawal
    balance *= 1 + interest_rate
    return balance


def seconds_in_days(days):
    """Return the number of seconds in `days` days."""
    seconds_per_minute = 60
    minutes_per_hour = 60
    hours_per_day = 24
    seconds_per_day = seconds_per_minute * minutes_per_hour * hours_per_day
    return days * seconds_per_day

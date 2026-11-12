"""Solutions for 02-01 Numbers and arithmetic."""


def total_cost(price, quantity):
    """Return the total cost of buying `quantity` items at `price` each."""
    return price * quantity


def whole_hours(minutes):
    """Return the number of whole hours in `minutes`."""
    return minutes // 60


def leftover_minutes(minutes):
    """Return the minutes left over after taking out the whole hours."""
    return minutes % 60


def average_of_three(first, second, third):
    """Return the average (mean) of three numbers."""
    # The brackets make the addition happen before the division.
    return (first + second + third) / 3


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def compound_growth(amount, rate, years):
    """Return the value of `amount` after `years` of growth at `rate` per year."""
    return amount * (1 + rate) ** years

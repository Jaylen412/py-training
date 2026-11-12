"""Solutions for 03-03 while loops."""


def countdown_text(start):
    """Return a countdown such as "3 2 1 Go!"."""
    text = ""
    current = start
    while current > 0:
        text += str(current) + " "
        current -= 1
    return text + "Go!"


def sum_of_digits(number):
    """Return the sum of the digits of a whole number."""
    total = 0
    while number > 0:
        total += number % 10   # last digit
        number //= 10          # drop the last digit
    return total


def count_halvings(number):
    """Return how many halvings it takes for `number` to drop below 1."""
    halvings = 0
    while number >= 1:
        number /= 2
        halvings += 1
    return halvings


def first_power_of_two_over(limit):
    """Return the smallest power of two greater than `limit`."""
    power = 1
    while power <= limit:
        power *= 2
    return power


def collatz_steps(number):
    """Return how many Collatz steps it takes to reach 1."""
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        steps += 1
    return steps

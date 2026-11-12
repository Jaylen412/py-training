"""Solutions for 03-04 for loops and range."""


def sum_up_to(number):
    """Return 1 + 2 + ... + number."""
    total = 0
    for value in range(1, number + 1):  # + 1 because range excludes the stop
        total += value
    return total


def factorial(number):
    """Return the factorial of `number`."""
    # Start from 1, not 0: multiplying by 0 would wipe out the result.
    product = 1
    for value in range(2, number + 1):
        product *= value
    return product


def count_vowels(text):
    """Return how many vowels are in `text`, ignoring case."""
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def times_table_row(number):
    """Return number x 1 up to number x 10, separated by spaces."""
    row = ""
    for multiplier in range(1, 11):
        row += str(number * multiplier) + " "
    return row.strip()  # remove the extra space after the last number


def triangle(height):
    """Return a triangle of stars as one string."""
    shape = ""
    for size in range(1, height + 1):
        shape += "*" * size + "\n"
    return shape


def sum_of_multiples(limit):
    """Return the sum of the multiples of 3 or 5 below `limit`."""
    total = 0
    for number in range(1, limit):
        if number % 3 == 0 or number % 5 == 0:
            total += number
    return total

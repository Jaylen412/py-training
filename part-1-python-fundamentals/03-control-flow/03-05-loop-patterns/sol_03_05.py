"""Solutions for 03-05 Loop patterns."""


def count_char(text, target):
    """Return how many times `target` appears in `text`."""
    count = 0
    for character in text:
        if character == target:
            count += 1
    return count


def index_of(text, target):
    """Return the index of the first `target` in `text`, or -1."""
    for index, character in enumerate(text):
        if character == target:
            return index  # returning also ends the loop
    return -1


def largest_digit(digits):
    """Return the largest digit in a string of digits."""
    largest = int(digits[0])
    for character in digits:
        value = int(character)
        if value > largest:
            largest = value
    return largest


def is_prime(number):
    """Return True if `number` is prime."""
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def all_digits(text):
    """Return True if every character in `text` is a digit."""
    if text == "":
        return False
    all_match = True
    for character in text:
        if not character.isdigit():
            all_match = False
            break
    return all_match


def last_index_of(text, target):
    """Return the index of the last `target` in `text`, or -1."""
    # Keep overwriting the answer, so the last match wins.
    found_at = -1
    for index, character in enumerate(text):
        if character == target:
            found_at = index
    return found_at

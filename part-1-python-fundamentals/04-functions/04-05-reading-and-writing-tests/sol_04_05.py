"""Solutions for 04-05 Reading and writing tests."""


def clamp(value, low, high):
    """Return `value` pushed into the range `low` to `high`."""
    if value < low:
        return low
    if value > high:
        return high
    return value


def is_palindrome(text):
    """Return True if `text` reads the same both ways, ignoring case and spaces."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def median_of_three(first, second, third):
    """Return the middle value of three numbers."""
    # The middle value is between the other two (inclusive, to handle ties).
    if first <= second <= third or third <= second <= first:
        return second
    if second <= first <= third or third <= first <= second:
        return first
    return third

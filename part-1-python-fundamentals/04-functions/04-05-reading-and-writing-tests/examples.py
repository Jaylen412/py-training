# 04-05 Reading and writing tests


def clamp(value, low, high):
    """Return value, pushed into the range low to high."""
    if value < low:
        return low
    if value > high:
        return high
    return value


# Example 1: assert does nothing when the condition is true
assert clamp(5, 0, 10) == 5
assert clamp(-3, 0, 10) == 0
assert clamp(42, 0, 10) == 10
print("All asserts passed")

# Example 2: assert with a message, for when it fails
result = clamp(15, 0, 10)
assert result == 10, f"expected 10 but got {result}"
print("Still passing")


# Example 3: a pytest-style test is a function whose name starts with test_
def test_clamp_inside_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_below_range():
    assert clamp(-3, 0, 10) == 0


def test_clamp_on_the_edges():
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


# pytest finds and calls these for you. Here we call them by hand.
test_clamp_inside_range()
test_clamp_below_range()
test_clamp_on_the_edges()
print("All test functions passed")

# Example 4: comparing floats in tests - check the difference is tiny
total = 0.1 + 0.2
assert abs(total - 0.3) < 1e-9
print("Float comparison passed")

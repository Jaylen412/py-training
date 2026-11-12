"""Solutions for 10-02 Iterators and generators."""


def countdown(start):
    """Yield start down to 1."""
    while start >= 1:
        yield start
        start -= 1


def parse_numbers(lines):
    """Yield floats from non-blank, non-comment lines."""
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        yield float(line)


def chunked(items, size):
    """Yield lists of `size` items."""
    if size < 1:
        raise ValueError(f"size must be at least 1, got {size}")
    for start in range(0, len(items), size):
        yield items[start:start + size]


def running_average(numbers):
    """Yield the average so far after each number."""
    total = 0
    for count, number in enumerate(numbers, start=1):
        total += number
        yield total / count


def take(iterable, count):
    """Return the first `count` items of `iterable`."""
    result = []
    iterator = iter(iterable)
    for _ in range(count):
        try:
            result.append(next(iterator))
        except StopIteration:
            break
    return result

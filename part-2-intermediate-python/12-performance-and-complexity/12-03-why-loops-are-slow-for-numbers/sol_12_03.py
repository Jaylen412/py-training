"""Solutions for 12-03 Why loops are slow for numbers."""


def mean(values):
    """Return the average of a non-empty list."""
    if not values:
        raise ValueError("cannot take the mean of an empty list")
    return sum(values) / len(values)


def _check_same_length(first, second):
    if len(first) != len(second):
        raise ValueError(f"lengths differ: {len(first)} and {len(second)}")


def dot_product(first, second):
    """Return the sum of item-by-item products."""
    _check_same_length(first, second)
    return sum(a * b for a, b in zip(first, second))


def elementwise_add(first, second):
    """Return the item-by-item sums."""
    _check_same_length(first, second)
    return [a + b for a, b in zip(first, second)]


def standardise(values):
    """Return the z-score of each value."""
    average = mean(values)
    spread = mean([(value - average) ** 2 for value in values]) ** 0.5
    if spread == 0:
        return [0.0 for _ in values]
    return [(value - average) / spread for value in values]


def matrix_vector_multiply(matrix, vector):
    """Return the dot product of each row with `vector`."""
    return [dot_product(row, vector) for row in matrix]

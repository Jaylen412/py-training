"""Exercises for 12-03 Why loops are slow for numbers.

Plain Python versions of operations you will vectorise with NumPy in Module 13.
"""


def mean(values):
    """Return the average of a non-empty list. Raise ValueError if empty.

    Example: mean([1, 2, 6]) returns 3.0
    """
    raise NotImplementedError


def dot_product(first, second):
    """Multiply the lists item by item and return the sum of the products.
    Raise ValueError if the lists have different lengths.

    Example: dot_product([1, 2, 3], [4, 5, 6]) returns 32  (4 + 10 + 18)
    """
    raise NotImplementedError


def elementwise_add(first, second):
    """Return a new list where each item is the sum of the items at the same
    position. Raise ValueError if the lengths differ.

    Example: elementwise_add([1, 2], [10, 20]) returns [11, 22]
    """
    raise NotImplementedError


def standardise(values):
    """Return the z-score of each value: (value - mean) / standard deviation,
    where standard deviation is the square root of the mean of the squared
    differences from the mean. If the standard deviation is 0, return a list
    of 0.0 values.

    Example: standardise([2, 4, 4, 4, 5, 5, 7, 9]) returns
    [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]
    """
    raise NotImplementedError


def matrix_vector_multiply(matrix, vector):
    """`matrix` is a list of rows (each a list of numbers). Return a list with
    one number per row: the dot product of that row with `vector`.
    Raise ValueError if any row's length differs from the vector's.

    Example: matrix_vector_multiply([[1, 2], [3, 4]], [10, 1]) returns [12, 34]
    """
    raise NotImplementedError

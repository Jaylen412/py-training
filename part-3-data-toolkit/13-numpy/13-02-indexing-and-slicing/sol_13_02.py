"""Solutions for 13-02 Indexing and slicing."""
import numpy as np


def column(table, index):
    """Return one column as a 1-D array."""
    return table[:, index]


def last_rows(table, count):
    """Return the last `count` rows."""
    if count == 0:
        return table[:0]  # table[-0:] would be the whole table
    return table[-count:]


def values_between(values, low, high):
    """Return the values within [low, high]."""
    return values[(values >= low) & (values <= high)]


def replace_below(values, floor):
    """Return a copy with values below `floor` raised to it."""
    result = values.copy()
    result[result < floor] = floor
    return result


def rows_where(table, column_index, threshold):
    """Return the rows whose chosen column exceeds `threshold`."""
    return table[table[:, column_index] > threshold]


def pick_rows(table, positions):
    """Return the rows at `positions`, in order."""
    return table[positions]

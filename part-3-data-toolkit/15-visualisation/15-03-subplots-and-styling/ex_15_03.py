"""Exercises for 15-03 Subplots and styling. Each function returns a Figure."""
import matplotlib.pyplot as plt


def small_multiples(frame, group_column, value_column):
    """Return a figure with ONE ROW of subplots, one per distinct value of
    `group_column` in sorted order. Each subplot shows a histogram of
    `value_column` for that group and has the group value as its title.
    All subplots share the y axis (sharey=True).
    """
    raise NotImplementedError


def highlight_bars(values, highlight, title):
    """`values` is a pandas Series. Return a figure with a horizontal bar chart
    (barh) of the values in their given order. The bar for the label
    `highlight` is coloured "tab:orange" and every other bar "lightgrey".
    """
    raise NotImplementedError


def mark_maximum(values, title):
    """`values` is a pandas Series. Return a figure with a line plot of the
    values against their index, and an annotation whose text is
    f"Max: {maximum}" pointing at the highest point.
    """
    raise NotImplementedError

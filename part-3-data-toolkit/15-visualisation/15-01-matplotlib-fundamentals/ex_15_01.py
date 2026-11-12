"""Exercises for 15-01 Matplotlib fundamentals.

Each chart function returns the Figure. Do not call plt.show().
"""
import matplotlib.pyplot as plt


def line_chart(x, y, title, x_label, y_label):
    """Return a figure with one line of y against x, and the given title and
    axis labels."""
    raise NotImplementedError


def multi_line_chart(x, lines, title):
    """`lines` is a dictionary mapping a label to a list of y values.
    Return a figure with one line per entry (in dictionary order), each with
    its label, plus a legend and the title."""
    raise NotImplementedError


def scatter_chart(x, y, title, x_label, y_label):
    """Return a figure with a scatter plot of y against x, and the given title
    and axis labels."""
    raise NotImplementedError


def save_figure(figure, path):
    """Save `figure` to `path` (a pathlib.Path), creating the parent folder
    if it does not exist. Then close the figure. Return the path."""
    raise NotImplementedError

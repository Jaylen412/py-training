"""Exercises for 15-02 Chart types and when to use them."""
import matplotlib.pyplot as plt


def choose_chart(question):
    """Return the best chart type for a kind of question:
    "compare categories" -> "bar"
    "distribution" -> "histogram"
    "compare distributions" -> "box"
    "relationship" -> "scatter"
    "over time" -> "line"
    Raise ValueError for any other question.
    """
    raise NotImplementedError


def bar_chart(values, title):
    """`values` is a pandas Series (index = category labels). Return a figure
    with a VERTICAL bar chart of the values sorted from largest to smallest,
    and the given title."""
    raise NotImplementedError


def histogram(values, bins, title):
    """Return a figure with a histogram of `values` using `bins` bins, and the
    given title."""
    raise NotImplementedError


def box_by_group(frame, value_column, group_column):
    """Return a figure with one box plot of `value_column` for each distinct
    value of `group_column`, in sorted order of the group values, labelled
    with the group values. Pass tick_labels= to ax.boxplot.
    """
    raise NotImplementedError

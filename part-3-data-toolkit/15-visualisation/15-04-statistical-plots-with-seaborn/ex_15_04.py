"""Exercises for 15-04 Statistical plots with seaborn."""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine


def wine_frame():
    """Return the wine dataset as one DataFrame (load_wine(as_frame=True).frame)
    with an extra column "cultivar" holding the class NAME for each row
    ("class_0", "class_1" or "class_2")."""
    raise NotImplementedError


def strongest_correlations(frame, target, count):
    """Return a pandas Series of the `count` columns (other than `target`)
    whose correlation with `target` has the largest ABSOLUTE value, sorted
    from strongest to weakest by absolute value. Keep the sign of each
    correlation in the values. Only use numeric columns.

    Example: for the wine data with target="target" and count=3, the first
    entry is "flavanoids" with value about -0.85
    """
    raise NotImplementedError


def hue_scatter(frame, x, y, hue):
    """Return a figure with a seaborn scatterplot of y against x, coloured by
    the `hue` column, with the title f"{y} against {x}"."""
    raise NotImplementedError


def correlation_heatmap(frame, columns):
    """Return a figure with a seaborn heatmap of the correlations between
    `columns`, with the numbers written in the cells (annot=True), and a
    colour scale from -1 to 1."""
    raise NotImplementedError

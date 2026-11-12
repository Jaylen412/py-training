"""Solutions for 15-04 Statistical plots with seaborn."""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine


def wine_frame():
    """Return the wine data with a cultivar name column."""
    wine = load_wine(as_frame=True)
    frame = wine.frame.copy()
    frame["cultivar"] = frame["target"].map(dict(enumerate(wine.target_names)))
    return frame


def strongest_correlations(frame, target, count):
    """Return the features most strongly correlated with `target`."""
    correlations = frame.select_dtypes(include="number").corr()[target].drop(target)
    # Sort by size of the correlation, ignoring its sign.
    order = correlations.abs().sort_values(ascending=False).index
    return correlations[order][:count]


def hue_scatter(frame, x, y, hue):
    """Return a scatter plot coloured by a category."""
    fig, ax = plt.subplots()
    sns.scatterplot(data=frame, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(f"{y} against {x}")
    return fig


def correlation_heatmap(frame, columns):
    """Return an annotated correlation heatmap."""
    fig, ax = plt.subplots()
    sns.heatmap(frame[columns].corr(), annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
    return fig

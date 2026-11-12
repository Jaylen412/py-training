"""Solutions for 15-03 Subplots and styling."""
import matplotlib.pyplot as plt


def small_multiples(frame, group_column, value_column):
    """One histogram per group, in a row, sharing the y axis."""
    groups = sorted(frame[group_column].unique())
    # squeeze=False always returns a 2-D array, even for a single group.
    fig, axes = plt.subplots(1, len(groups), sharey=True, squeeze=False, figsize=(3 * len(groups), 3))
    for ax, group in zip(axes.flat, groups):
        ax.hist(frame.loc[frame[group_column] == group, value_column])
        ax.set_title(str(group))
    fig.tight_layout()
    return fig


def highlight_bars(values, highlight, title):
    """Horizontal bars with one highlighted."""
    colours = ["tab:orange" if label == highlight else "lightgrey" for label in values.index]
    fig, ax = plt.subplots()
    ax.barh(values.index, values.values, color=colours)
    ax.set_title(title)
    return fig


def mark_maximum(values, title):
    """Line chart with the maximum annotated."""
    fig, ax = plt.subplots()
    ax.plot(values.index, values.values)
    peak = values.idxmax()
    ax.annotate(f"Max: {values.max()}", xy=(peak, values.max()), arrowprops={"arrowstyle": "->"})
    ax.set_title(title)
    return fig

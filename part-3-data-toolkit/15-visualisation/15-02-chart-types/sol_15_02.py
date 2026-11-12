"""Solutions for 15-02 Chart types and when to use them."""
import matplotlib.pyplot as plt

CHARTS = {
    "compare categories": "bar",
    "distribution": "histogram",
    "compare distributions": "box",
    "relationship": "scatter",
    "over time": "line",
}


def choose_chart(question):
    """Return the chart type for a kind of question."""
    if question not in CHARTS:
        raise ValueError(f"unknown kind of question: {question!r}")
    return CHARTS[question]


def bar_chart(values, title):
    """Return a sorted vertical bar chart."""
    ordered = values.sort_values(ascending=False)
    fig, ax = plt.subplots()
    ax.bar(ordered.index, ordered.values)
    ax.set_title(title)
    return fig


def histogram(values, bins, title):
    """Return a histogram."""
    fig, ax = plt.subplots()
    ax.hist(values, bins=bins)
    ax.set_title(title)
    return fig


def box_by_group(frame, value_column, group_column):
    """Return one box per group, in sorted group order."""
    groups = sorted(frame[group_column].unique())
    data = [frame.loc[frame[group_column] == group, value_column] for group in groups]
    fig, ax = plt.subplots()
    ax.boxplot(data, tick_labels=groups)
    ax.set_ylabel(value_column)
    return fig

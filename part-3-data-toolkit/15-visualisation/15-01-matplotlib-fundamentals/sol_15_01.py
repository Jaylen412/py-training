"""Solutions for 15-01 Matplotlib fundamentals."""
import matplotlib.pyplot as plt


def _label(ax, title, x_label, y_label):
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


def line_chart(x, y, title, x_label, y_label):
    """Return a labelled line chart."""
    fig, ax = plt.subplots()
    ax.plot(x, y)
    _label(ax, title, x_label, y_label)
    return fig


def multi_line_chart(x, lines, title):
    """Return a chart with one labelled line per dictionary entry."""
    fig, ax = plt.subplots()
    for label, values in lines.items():
        ax.plot(x, values, label=label)
    ax.set_title(title)
    ax.legend()
    return fig


def scatter_chart(x, y, title, x_label, y_label):
    """Return a labelled scatter plot."""
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    _label(ax, title, x_label, y_label)
    return fig


def save_figure(figure, path):
    """Save a figure, creating its folder, then close it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path)
    plt.close(figure)
    return path

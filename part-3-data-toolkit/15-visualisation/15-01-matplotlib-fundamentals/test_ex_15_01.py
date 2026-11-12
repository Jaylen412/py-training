import importlib
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pytest  # noqa: E402

mod = importlib.import_module(
    "sol_15_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_15_01"
)


@pytest.fixture(autouse=True)
def close_figures():
    yield
    plt.close("all")


def test_line_chart():
    fig = mod.line_chart([1, 2, 3], [4, 5, 9], "Growth", "Year", "Value")
    ax = fig.axes[0]
    assert ax.get_title() == "Growth"
    assert (ax.get_xlabel(), ax.get_ylabel()) == ("Year", "Value")
    assert len(ax.get_lines()) == 1
    np.testing.assert_array_equal(ax.get_lines()[0].get_ydata(), [4, 5, 9])


def test_line_chart_returns_figure():
    assert isinstance(mod.line_chart([1], [1], "t", "x", "y"), matplotlib.figure.Figure)


def test_multi_line_chart():
    fig = mod.multi_line_chart([1, 2], {"London": [5, 6], "Glasgow": [3, 4]}, "Temps")
    ax = fig.axes[0]
    assert [line.get_label() for line in ax.get_lines()] == ["London", "Glasgow"]
    assert ax.get_legend() is not None
    assert ax.get_title() == "Temps"


def test_multi_line_chart_single_line():
    fig = mod.multi_line_chart([0, 1], {"only": [1, 1]}, "One")
    assert len(fig.axes[0].get_lines()) == 1


def test_scatter_chart():
    fig = mod.scatter_chart([1, 2, 3], [3, 1, 2], "Points", "x", "y")
    ax = fig.axes[0]
    assert len(ax.collections) == 1
    np.testing.assert_array_equal(ax.collections[0].get_offsets(), [[1, 3], [2, 1], [3, 2]])
    assert ax.get_title() == "Points" and ax.get_xlabel() == "x"


def test_scatter_chart_has_no_lines():
    fig = mod.scatter_chart([1], [1], "t", "x", "y")
    assert len(fig.axes[0].get_lines()) == 0


def test_save_figure_creates_folder(tmp_path):
    fig = mod.line_chart([1, 2], [1, 2], "t", "x", "y")
    path = tmp_path / "new_folder" / "chart.png"
    assert mod.save_figure(fig, path) == path
    assert path.exists() and path.stat().st_size > 0


def test_save_figure_closes_figure(tmp_path):
    fig = mod.line_chart([1, 2], [1, 2], "t", "x", "y")
    mod.save_figure(fig, tmp_path / "chart.png")
    assert fig.number not in plt.get_fignums()

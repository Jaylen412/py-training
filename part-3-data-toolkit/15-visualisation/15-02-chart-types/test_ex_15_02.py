import importlib
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import pytest  # noqa: E402

mod = importlib.import_module(
    "sol_15_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_15_02"
)


@pytest.fixture(autouse=True)
def close_figures():
    yield
    plt.close("all")


@pytest.mark.parametrize(
    "question, chart",
    [
        ("compare categories", "bar"),
        ("distribution", "histogram"),
        ("compare distributions", "box"),
        ("relationship", "scatter"),
        ("over time", "line"),
    ],
)
def test_choose_chart(question, chart):
    assert mod.choose_chart(question) == chart


def test_choose_chart_unknown():
    with pytest.raises(ValueError):
        mod.choose_chart("pie please")


def test_bar_chart_sorted():
    fig = mod.bar_chart(pd.Series({"Toys": 5, "Clothing": 20, "Food": 10}), "Sales")
    ax = fig.axes[0]
    heights = [patch.get_height() for patch in ax.patches]
    assert heights == [20, 10, 5]
    assert [label.get_text() for label in ax.get_xticklabels()] == ["Clothing", "Food", "Toys"]
    assert ax.get_title() == "Sales"


def test_bar_chart_single_bar():
    fig = mod.bar_chart(pd.Series({"Only": 3}), "One")
    assert len(fig.axes[0].patches) == 1


def test_histogram_bins():
    fig = mod.histogram([1, 2, 2, 3, 3, 3, 10], bins=3, title="Spread")
    ax = fig.axes[0]
    assert len(ax.patches) == 3
    assert sum(patch.get_height() for patch in ax.patches) == 7
    assert ax.get_title() == "Spread"


def test_histogram_one_bin():
    fig = mod.histogram([5, 6, 7], bins=1, title="t")
    assert fig.axes[0].patches[0].get_height() == 3


def test_box_by_group():
    frame = pd.DataFrame({"group": ["b", "a", "b", "a", "c"], "value": [1, 2, 3, 4, 5]})
    fig = mod.box_by_group(frame, "value", "group")
    ax = fig.axes[0]
    assert [label.get_text() for label in ax.get_xticklabels()] == ["a", "b", "c"]
    low, high = ax.get_ylim()
    assert low <= 1 and high >= 5

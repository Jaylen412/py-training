import importlib
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.colors as mcolors  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import pytest  # noqa: E402

mod = importlib.import_module(
    "sol_15_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_15_03"
)


@pytest.fixture(autouse=True)
def close_figures():
    yield
    plt.close("all")


@pytest.fixture
def frame():
    return pd.DataFrame({
        "store": ["S2", "S1", "S2", "S3", "S1", "S1"],
        "units": [5, 1, 7, 2, 3, 9],
    })


def test_small_multiples_one_panel_per_group(frame):
    fig = mod.small_multiples(frame, "store", "units")
    assert [ax.get_title() for ax in fig.axes] == ["S1", "S2", "S3"]


def test_small_multiples_share_y(frame):
    fig = mod.small_multiples(frame, "store", "units")
    first, second = fig.axes[0], fig.axes[1]
    assert first.get_shared_y_axes().joined(first, second)
    assert sum(patch.get_height() for patch in fig.axes[0].patches) == 3


def test_small_multiples_single_group():
    fig = mod.small_multiples(pd.DataFrame({"g": ["a", "a"], "v": [1, 2]}), "g", "v")
    assert len(fig.axes) == 1


def test_highlight_bars():
    values = pd.Series({"S3": 10, "S1": 30, "S2": 20})
    fig = mod.highlight_bars(values, "S1", "Revenue")
    ax = fig.axes[0]
    colours = [mcolors.to_hex(patch.get_facecolor()) for patch in ax.patches]
    assert colours == [mcolors.to_hex("lightgrey"), mcolors.to_hex("tab:orange"), mcolors.to_hex("lightgrey")]
    assert [patch.get_width() for patch in ax.patches] == [10, 30, 20]
    assert ax.get_title() == "Revenue"


def test_highlight_bars_missing_label_all_grey():
    fig = mod.highlight_bars(pd.Series({"a": 1}), "zzz", "t")
    assert mcolors.to_hex(fig.axes[0].patches[0].get_facecolor()) == mcolors.to_hex("lightgrey")


def test_mark_maximum():
    values = pd.Series([3, 9, 4], index=[10, 20, 30])
    fig = mod.mark_maximum(values, "Peak")
    ax = fig.axes[0]
    annotations = [text for text in ax.texts if isinstance(text, matplotlib.text.Annotation)]
    assert len(annotations) == 1
    assert annotations[0].get_text() == "Max: 9"
    assert tuple(annotations[0].xy) == (20, 9)
    assert len(ax.get_lines()) == 1

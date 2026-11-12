import importlib
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import pytest  # noqa: E402

mod = importlib.import_module(
    "sol_15_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_15_04"
)


@pytest.fixture(autouse=True)
def close_figures():
    yield
    plt.close("all")


def test_wine_frame():
    frame = mod.wine_frame()
    assert frame.shape == (178, 15)
    assert frame["cultivar"].value_counts().to_dict() == {"class_1": 71, "class_0": 59, "class_2": 48}


def test_wine_frame_matches_target():
    frame = mod.wine_frame()
    assert (frame.loc[frame["target"] == 2, "cultivar"] == "class_2").all()


def test_strongest_correlations_wine():
    result = mod.strongest_correlations(mod.wine_frame(), "target", 3)
    assert result.index.tolist() == ["flavanoids", "od280/od315_of_diluted_wines", "total_phenols"]
    assert result.iloc[0] == pytest.approx(-0.847, abs=0.001)


def test_strongest_correlations_keeps_sign_and_excludes_target():
    frame = pd.DataFrame({"t": [1, 2, 3, 4], "up": [2, 4, 6, 8.5], "down": [4, 3, 2, 1], "label": list("abcd")})
    result = mod.strongest_correlations(frame, "t", 5)
    assert "t" not in result.index
    assert result["down"] == pytest.approx(-1.0)
    assert result.index.tolist() == ["down", "up"]


def test_hue_scatter():
    frame = pd.DataFrame({"a": [1, 2, 3, 4], "b": [4, 3, 2, 1], "group": ["x", "x", "y", "y"]})
    fig = mod.hue_scatter(frame, "a", "b", "group")
    ax = fig.axes[0]
    assert ax.get_title() == "b against a"
    assert ax.get_legend() is not None
    assert (ax.get_xlabel(), ax.get_ylabel()) == ("a", "b")


def test_correlation_heatmap():
    frame = mod.wine_frame()
    columns = ["alcohol", "proline", "hue"]
    fig = mod.correlation_heatmap(frame, columns)
    ax = fig.axes[0]
    texts = [text.get_text() for text in ax.texts]
    assert len(texts) == 9
    assert "1.00" in texts and "0.64" in texts
    mesh = ax.collections[0]
    assert mesh.get_clim() == (-1, 1)

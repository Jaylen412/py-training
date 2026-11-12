import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_08_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_08_01"
)


def test_circle_area():
    assert mod.circle_area(1) == pytest.approx(3.141592653589793)
    assert mod.circle_area(2) == pytest.approx(12.566370614359172)


def test_circle_area_zero():
    assert mod.circle_area(0) == 0


def test_round_up():
    assert mod.round_up(3.2) == 4
    assert mod.round_up(3.0) == 3


def test_round_up_negative():
    assert mod.round_up(-3.7) == -3


def test_median_of_odd():
    assert mod.median_of([5, 1, 3]) == 3


def test_median_of_even():
    assert mod.median_of([1, 2, 3, 4]) == 2.5


def test_distance():
    assert mod.distance((0, 0), (3, 4)) == pytest.approx(5.0)


def test_distance_three_dimensions():
    assert mod.distance((1, 2, 3), (1, 2, 3)) == 0
    assert mod.distance((0, 0, 0), (2, 3, 6)) == pytest.approx(7.0)


def test_imported_modules():
    source = "import math\nfrom pathlib import Path\nx = 1"
    assert mod.imported_modules(source) == ["math", "pathlib"]


def test_imported_modules_alias_and_indent():
    source = "import numpy as np\n    import os\nprint('import me')\n"
    assert mod.imported_modules(source) == ["numpy", "os"]


def test_imported_modules_none():
    assert mod.imported_modules("") == []
    assert mod.imported_modules("x = 1\nimportant = 2") == []

import importlib
import os

import numpy as np
import pandas as pd
import pytest

mod = importlib.import_module(
    "sol_16_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_16_02"
)

KIDNEY = pd.DataFrame({
    "treatment": ["A", "A", "B", "B"],
    "stone_size": ["small", "large", "small", "large"],
    "patients": [87, 263, 270, 80],
    "recovered": [81, 192, 234, 55],
})


def test_iqr_bounds():
    assert mod.iqr_bounds(pd.Series([1, 2, 3, 4, 5, 6, 7, 8])) == pytest.approx((-2.5, 11.5))


def test_iqr_bounds_constant_values():
    assert mod.iqr_bounds(pd.Series([5, 5, 5])) == pytest.approx((5, 5))


def test_iqr_outliers():
    values = pd.Series([10, 12, 11, 13, 12, 95, -40])
    result = mod.iqr_outliers(values)
    assert result.tolist() == [95, -40]
    assert result.index.tolist() == [5, 6]


def test_iqr_outliers_none():
    assert len(mod.iqr_outliers(pd.Series([1, 2, 3, 4]))) == 0


def test_zscore_outliers():
    values = pd.Series([10] * 20 + [50])
    assert mod.zscore_outliers(values).tolist() == [50]


def test_zscore_outliers_threshold():
    values = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 30])
    assert len(mod.zscore_outliers(values, threshold=3)) == 0
    assert mod.zscore_outliers(values, threshold=2).tolist() == [30]


def test_log_transform():
    result = mod.log_transform(pd.Series([0, np.e - 1, 9]))
    np.testing.assert_allclose(result, [0, 1, np.log(10)])


def test_log_transform_reduces_skew():
    values = pd.Series(np.random.default_rng(42).lognormal(0, 1, 500))
    assert abs(mod.log_transform(values).skew()) < abs(values.skew())


def test_log_transform_rejects_negative():
    with pytest.raises(ValueError):
        mod.log_transform(pd.Series([1, -1]))


def test_success_rates_overall():
    result = mod.success_rates(KIDNEY, "treatment", "patients", "recovered")
    assert result.to_dict() == {"A": 0.78, "B": 0.826}


def test_success_rates_within_groups_reverses():
    result = mod.success_rates(KIDNEY, ["stone_size", "treatment"], "patients", "recovered")
    assert result[("small", "A")] > result[("small", "B")]
    assert result[("large", "A")] > result[("large", "B")]

import importlib
import logging
import os
import time
from types import SimpleNamespace

import pytest

mod = importlib.import_module(
    "sol_11_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_11_04"
)


def test_timer_measures_time():
    with mod.Timer() as timer:
        time.sleep(0.02)
    assert 0.015 < timer.elapsed < 1


def test_timer_does_not_hide_exceptions():
    timer = mod.Timer()
    with pytest.raises(ZeroDivisionError):
        with timer:
            1 / 0
    assert timer.elapsed is not None


def test_temporary_attribute():
    settings = SimpleNamespace(debug=False)
    with mod.temporary_attribute(settings, "debug", True) as target:
        assert target is settings
        assert settings.debug is True
    assert settings.debug is False


def test_temporary_attribute_restores_after_error():
    settings = SimpleNamespace(level=1)
    with pytest.raises(RuntimeError, match="boom"):
        with mod.temporary_attribute(settings, "level", 99):
            raise RuntimeError("boom")
    assert settings.level == 1


def test_ignore_errors_swallows_listed_types():
    with mod.ignore_errors(KeyError):
        {}["missing"]
    with mod.ignore_errors(KeyError, ValueError):
        int("abc")


def test_ignore_errors_lets_other_errors_through():
    with pytest.raises(ZeroDivisionError):
        with mod.ignore_errors(KeyError):
            1 / 0


def test_ignore_errors_without_error_runs_block():
    ran = []
    with mod.ignore_errors(KeyError):
        ran.append(True)
    assert ran == [True]


# caplog is a pytest fixture that captures log messages.
def test_process_orders_returns_valid_ids(caplog):
    logger = logging.getLogger("test_orders")
    with caplog.at_level(logging.INFO, logger="test_orders"):
        result = mod.process_orders([(1, 2), (2, 0), (3, 5), (4, "x")], logger)
    assert result == [1, 3]


def test_process_orders_logs_warnings_and_summary(caplog):
    logger = logging.getLogger("test_orders")
    with caplog.at_level(logging.INFO, logger="test_orders"):
        mod.process_orders([(1, 2), (2, 0)], logger)
    warnings = [r.getMessage() for r in caplog.records if r.levelno == logging.WARNING]
    infos = [r.getMessage() for r in caplog.records if r.levelno == logging.INFO]
    assert len(warnings) == 1 and "2" in warnings[0]
    assert len(infos) == 1 and "processed 1 of 2" in infos[0]


def test_process_orders_empty(caplog):
    logger = logging.getLogger("test_orders")
    with caplog.at_level(logging.INFO, logger="test_orders"):
        assert mod.process_orders([], logger) == []
    assert any("processed 0 of 0" in r.getMessage() for r in caplog.records)

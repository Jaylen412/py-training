import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_11_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_11_03"
)


# The messy versions from the docstrings, used as the reference behaviour.
def messy_shipping(w, e=False):
    if w <= 0:
        raise ValueError("bad")
    if w <= 2:
        c = 4.5
    elif w <= 10:
        c = 4.5 + (w - 2) * 1.25
    else:
        c = 4.5 + 8 * 1.25 + (w - 10) * 0.8
    if e:
        c = c * 1.5
    return round(c, 2)


def messy_receipt(lines):
    s = ""
    for x in lines:
        s = s + x[0].ljust(10) + str(x[1]).rjust(3) + " x " + ("%.2f" % x[2]).rjust(6) + "\n"
    s = s + "TOTAL".ljust(10) + ("%.2f" % sum([x[1] * x[2] for x in lines])).rjust(12) + "\n"
    return s


@pytest.mark.parametrize("weight", [0.5, 2, 2.5, 5, 10, 10.5, 25])
@pytest.mark.parametrize("express", [False, True])
def test_shipping_cost_matches_original(weight, express):
    assert mod.shipping_cost(weight, express) == pytest.approx(messy_shipping(weight, express))


def test_shipping_cost_example():
    assert mod.shipping_cost(5) == pytest.approx(8.25)


@pytest.mark.parametrize("weight", [0, -1])
def test_shipping_cost_rejects_bad_weight(weight):
    with pytest.raises(ValueError):
        mod.shipping_cost(weight)


def test_order_summary():
    lines = [("pen", 2, 1.5), ("pad", 1, 4.0)]
    assert mod.order_summary(lines) == {"total": 7.0, "items": 3, "most_expensive": "pad"}


def test_order_summary_empty():
    assert mod.order_summary([]) == {"total": 0, "items": 0, "most_expensive": None}


def test_order_summary_tie_keeps_first():
    lines = [("a", 1, 2.0), ("b", 1, 2.0)]
    assert mod.order_summary(lines)["most_expensive"] == "a"


def test_format_receipt_example():
    assert mod.format_receipt([("pen", 2, 1.5)]) == "pen         2 x   1.50\nTOTAL             3.00\n"


@pytest.mark.parametrize(
    "lines",
    [[], [("notebook", 12, 3.25), ("pen", 1, 0.99)], [("x", 100, 123.456)]],
)
def test_format_receipt_matches_original(lines):
    assert mod.format_receipt(lines) == messy_receipt(lines)

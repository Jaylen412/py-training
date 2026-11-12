import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_09_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_09_04"
)


def test_line_item_fields_and_total():
    item = mod.LineItem("Pen", 1.5, 4)
    assert (item.description, item.unit_price, item.quantity) == ("Pen", 1.5, 4)
    assert item.total == pytest.approx(6.0)


def test_line_item_default_quantity_and_repr():
    item = mod.LineItem("Pad", 2.0)
    assert item.quantity == 1
    assert repr(item) == "LineItem(description='Pad', unit_price=2.0, quantity=1)"
    assert item == mod.LineItem("Pad", 2.0, 1)


def test_line_item_total_follows_changes():
    item = mod.LineItem("Pen", 1.5, 4)
    item.quantity = 10
    assert item.total == pytest.approx(15.0)


def test_invoice_totals():
    invoice = mod.Invoice("Ada")
    invoice.add(mod.LineItem("Pen", 1.5, 4))
    invoice.add(mod.LineItem("Pad", 2.0))
    assert invoice.subtotal == pytest.approx(8.0)
    assert invoice.tax == pytest.approx(1.6)
    assert invoice.total == pytest.approx(9.6)


def test_invoice_custom_tax_rate():
    invoice = mod.Invoice("Alan", tax_rate=0.05)
    invoice.add(mod.LineItem("Book", 10.0, 3))
    assert invoice.total == pytest.approx(31.5)


def test_invoices_do_not_share_items():
    first = mod.Invoice("Ada")
    second = mod.Invoice("Alan")
    first.add(mod.LineItem("Pen", 1.0))
    assert second.items == []
    assert second.total == 0


def test_bounded_value_inside_range():
    bounded = mod.BoundedValue(5, 0, 10)
    assert bounded.value == 5
    bounded.value = 7
    assert bounded.value == 7


def test_bounded_value_clamps():
    bounded = mod.BoundedValue(15, 0, 10)
    assert bounded.value == 10
    bounded.value = -3
    assert bounded.value == 0


def test_bounded_value_bad_range():
    with pytest.raises(ValueError):
        mod.BoundedValue(5, 10, 0)

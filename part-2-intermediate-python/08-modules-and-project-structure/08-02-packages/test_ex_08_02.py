import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_08_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_08_02"
)


def test_module_name_from_path():
    assert mod.module_name_from_path("shop/pricing.py") == "shop.pricing"
    assert mod.module_name_from_path("a/b/c.py") == "a.b.c"


def test_module_name_from_path_init():
    assert mod.module_name_from_path("shop/__init__.py") == "shop"
    assert mod.module_name_from_path("tools.py") == "tools"


def test_resolve_relative_same_package():
    assert mod.resolve_relative("shop.cart", ".pricing") == "shop.pricing"


def test_resolve_relative_up_one_level():
    assert mod.resolve_relative("shop.sales.cart", "..pricing") == "shop.pricing"
    assert mod.resolve_relative("a.b.c.d", "..x") == "a.b.x"


def test_is_valid_module_name():
    assert mod.is_valid_module_name("shop.pricing") is True
    assert mod.is_valid_module_name("math") is True


def test_is_valid_module_name_invalid():
    assert mod.is_valid_module_name("shop..pricing") is False
    assert mod.is_valid_module_name("2nd.module") is False
    assert mod.is_valid_module_name("my-module") is False
    assert mod.is_valid_module_name("") is False


def test_discounted_cart_total():
    assert mod.discounted_cart_total([10, 20], 0.5) == pytest.approx(18.0)


def test_discounted_cart_total_no_discount_and_empty():
    assert mod.discounted_cart_total([10], 0) == pytest.approx(12.0)
    assert mod.discounted_cart_total([], 0.2) == 0

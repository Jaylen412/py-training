"""Exercises for 08-02 Packages.

The `shop` package is in this folder, next to this file.
"""


def module_name_from_path(path):
    """Turn a relative file path using "/" into a dotted module name.
    A path ending in "/__init__.py" names the package itself.

    Example: module_name_from_path("shop/pricing.py") returns "shop.pricing"
    Example: module_name_from_path("shop/__init__.py") returns "shop"
    """
    raise NotImplementedError


def resolve_relative(current_module, relative_name):
    """Return the absolute module name that a relative import refers to.
    `current_module` is the full name of the module doing the import.
    One leading dot means the current module's package; each extra dot goes
    up one more package level.

    Example: resolve_relative("shop.cart", ".pricing") returns "shop.pricing"
    Example: resolve_relative("shop.sales.cart", "..pricing") returns "shop.pricing"
    """
    raise NotImplementedError


def is_valid_module_name(name):
    """Return True if `name` is one or more valid Python identifiers joined
    by single dots. The string method isidentifier() checks one part:
    "pricing".isidentifier() is True, "2nd".isidentifier() is False.

    Example: is_valid_module_name("shop.pricing") returns True
    Example: is_valid_module_name("shop..pricing") returns False
    """
    raise NotImplementedError


def discounted_cart_total(prices, rate):
    """Apply `rate` as a discount to each price with
    shop.pricing.apply_discount, then return shop.cart_total of the
    discounted prices. Import what you need from the shop package.

    Example: discounted_cart_total([10, 20], 0.5) returns 18.0
    """
    raise NotImplementedError

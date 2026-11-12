"""Solutions for 08-02 Packages."""
from shop import cart_total
from shop.pricing import apply_discount


def module_name_from_path(path):
    """Turn a file path into a dotted module name."""
    parts = path.removesuffix(".py").split("/")
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def resolve_relative(current_module, relative_name):
    """Return the absolute module name of a relative import."""
    dots = len(relative_name) - len(relative_name.lstrip("."))
    target = relative_name[dots:]
    # Dropping the module's own name gives its package (one dot);
    # every extra dot drops one more level.
    package_parts = current_module.split(".")[:-dots]
    return ".".join(package_parts + [target])


def is_valid_module_name(name):
    """Return True if `name` is dot-separated identifiers."""
    parts = name.split(".")
    return all([part.isidentifier() for part in parts])


def discounted_cart_total(prices, rate):
    """Return the cart total of the discounted prices."""
    discounted = [apply_discount(price, rate) for price in prices]
    return cart_total(discounted)

"""Exercises for 05-05 Nested data and references.

Products are dictionaries with the keys "name", "price" and "quantity".
"""


def total_value(products):
    """Return the sum of price x quantity over all products.

    Example: total_value([{"name": "Pen", "price": 1.5, "quantity": 10}])
    returns 15.0
    """
    raise NotImplementedError


def cheapest_product(products):
    """Return the name of the product with the lowest price.
    If several share the lowest price, return the first. Return None if
    the list is empty.

    Example: for Pen (1.5) and Stapler (7.0), returns "Pen"
    """
    raise NotImplementedError


def names_by_city(people):
    """`people` is a list of (name, city) tuples. Return a dictionary
    mapping each city to a list of names, in the order they appear.

    Example: names_by_city([("Ada", "London"), ("Alan", "Leeds"), ("Grace", "London")])
    returns {"London": ["Ada", "Grace"], "Leeds": ["Alan"]}
    """
    raise NotImplementedError


def doubled(numbers):
    """Return a NEW list with every number doubled. The list passed in
    must not change.

    Example: doubled([1, 2, 3]) returns [2, 4, 6]
    """
    raise NotImplementedError


def copy_grid(grid):
    """Return a copy of a list of lists that shares NO lists with the
    original, so changing the copy never changes `grid`.
    Do not use the copy module: copy each row yourself.

    Example: copy_grid([[1, 2], [3, 4]]) returns [[1, 2], [3, 4]]
    """
    raise NotImplementedError

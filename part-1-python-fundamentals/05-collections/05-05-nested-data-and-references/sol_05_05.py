"""Solutions for 05-05 Nested data and references."""


def total_value(products):
    """Return the sum of price x quantity over all products."""
    total = 0
    for product in products:
        total += product["price"] * product["quantity"]
    return total


def cheapest_product(products):
    """Return the name of the cheapest product, or None if there are none."""
    if len(products) == 0:
        return None
    cheapest = products[0]
    for product in products:
        if product["price"] < cheapest["price"]:  # strict < keeps the first on ties
            cheapest = product
    return cheapest["name"]


def names_by_city(people):
    """Group names by city."""
    groups = {}
    for name, city in people:
        if city not in groups:
            groups[city] = []
        groups[city].append(name)
    return groups


def doubled(numbers):
    """Return a new list with every number doubled."""
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def copy_grid(grid):
    """Return a copy of a list of lists that shares no inner lists."""
    new_grid = []
    for row in grid:
        new_grid.append(row[:])  # a slice makes a new inner list
    return new_grid

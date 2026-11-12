# 04-04 Functions as building blocks
# Problem: produce a receipt line for an item, with a discount for
# members and tax added on top.


# Example 1: small, single-purpose functions with type hints
def apply_discount(price: float, discount_rate: float) -> float:
    """Return the price after taking off discount_rate (0.1 means 10%)."""
    return price * (1 - discount_rate)


def add_tax(price: float, tax_rate: float) -> float:
    """Return the price with tax added (0.2 means 20%)."""
    return price * (1 + tax_rate)


def format_money(amount: float) -> str:
    """Return the amount as a string such as $12.50."""
    return f"${amount:,.2f}"


# Example 2: a higher-level function built from the small ones
def receipt_line(item: str, price: float, is_member: bool) -> str:
    """Return one line of a receipt."""
    discount_rate = 0.1 if is_member else 0.0
    discounted = apply_discount(price, discount_rate)
    final_price = add_tax(discounted, 0.2)
    return f"{item:<10}{format_money(final_price):>10}"


print(receipt_line("Coffee", 3.50, True))
print(receipt_line("Sandwich", 6.00, False))
print(receipt_line("Cake", 2.75, True))

# Example 3: each small piece can be checked on its own
print(apply_discount(100, 0.1))
print(add_tax(100, 0.2))
print(format_money(1234.5))


# Example 4: a pure function versus an impure one
def pure_total(prices_text: str) -> float:
    """Add up comma-separated prices. Depends only on its argument."""
    total = 0.0
    for piece in prices_text.split(","):
        total += float(piece)
    return total


running_total = 0.0


def impure_add(price: float) -> float:
    """Changes a global variable - the same call gives different answers."""
    global running_total
    running_total += price
    return running_total


print(pure_total("1.50,2.25"), pure_total("1.50,2.25"))
print(impure_add(1.5), impure_add(1.5))


# Example 5: type hints are documentation; Python does not enforce them
print(format_money(7))
print(add_tax("ab", 2))

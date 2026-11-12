"""Solutions for 04-03 Scope."""


def add_points(score, points):
    """Return the new score."""
    return score + points


def price_with_tax(price, tax_rate=0.2):
    """Return the price with tax added."""
    return price * (1 + tax_rate)


def count_long_words(text, min_length):
    """Return how many words have at least `min_length` letters."""
    count = 0
    for word in text.split():
        if len(word) >= min_length:
            count += 1
    return count


def apply_transaction(balance, amount, is_deposit):
    """Return the balance after a deposit or withdrawal."""
    if is_deposit:
        return balance + amount
    return balance - amount

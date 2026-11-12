"""Solutions for 09-02 Special methods."""


class Money:
    """An amount of money in a currency."""

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def _check_same_currency(self, other):
        # A leading underscore marks a helper meant for use inside the class.
        if self.currency != other.currency:
            raise ValueError(f"cannot mix {self.currency} and {other.currency}")

    def __lt__(self, other):
        self._check_same_currency(other)
        return self.amount < other.amount

    def __add__(self, other):
        self._check_same_currency(other)
        return Money(self.amount + other.amount, self.currency)


class Deck:
    """A deck of cards."""

    def __init__(self, cards):
        self.cards = list(cards)

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck({len(self)} cards)"

    def draw(self):
        if not self.cards:
            raise IndexError("cannot draw from an empty deck")
        return self.cards.pop()

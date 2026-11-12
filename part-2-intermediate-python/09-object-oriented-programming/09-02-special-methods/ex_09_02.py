"""Exercises for 09-02 Special methods."""


class Money:
    """An amount of money in a currency, such as Money(5, "USD")."""

    def __init__(self, amount, currency):
        """Store amount (as given) and currency as attributes."""
        raise NotImplementedError

    def __repr__(self):
        """Example: repr(Money(5, "USD")) returns "Money(5, 'USD')" """
        raise NotImplementedError

    def __str__(self):
        """Return the amount with 2 decimal places, a space, then the currency.

        Example: str(Money(5, "USD")) returns "5.00 USD"
        """
        raise NotImplementedError

    def __eq__(self, other):
        """Equal if `other` is a Money with the same amount and currency.
        Return NotImplemented if `other` is not a Money.
        """
        raise NotImplementedError

    def __lt__(self, other):
        """Compare amounts. Raise ValueError if the currencies differ."""
        raise NotImplementedError

    def __add__(self, other):
        """Return a NEW Money with the amounts added.
        Raise ValueError if the currencies differ.

        Example: Money(5, "USD") + Money(2.5, "USD") equals Money(7.5, "USD")
        """
        raise NotImplementedError


class Deck:
    """A deck of cards (any strings, such as "AS" for the ace of spades)."""

    def __init__(self, cards):
        """Store a COPY of `cards` as a list attribute called cards."""
        raise NotImplementedError

    def __len__(self):
        """Return the number of cards left."""
        raise NotImplementedError

    def __repr__(self):
        """Example: repr(Deck(["AS", "KH"])) returns "Deck(2 cards)" """
        raise NotImplementedError

    def draw(self):
        """Remove and return the top card (the LAST item of the list).
        Raise IndexError with a clear message if the deck is empty.
        """
        raise NotImplementedError

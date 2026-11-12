import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_09_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_09_02"
)
Money = mod.Money
Deck = mod.Deck


def test_money_repr_and_str():
    money = Money(5, "USD")
    assert repr(money) == "Money(5, 'USD')"
    assert str(money) == "5.00 USD"
    assert f"{Money(1234.5, 'EUR')}" == "1234.50 EUR"


def test_money_equality():
    assert Money(5, "USD") == Money(5, "USD")
    assert Money(5, "USD") != Money(5, "EUR")
    assert Money(5, "USD") != Money(6, "USD")


def test_money_not_equal_to_other_types():
    assert Money(5, "USD") != 5
    assert Money(5, "USD") != "5.00 USD"


def test_money_sorting():
    wallet = [Money(10, "USD"), Money(2, "USD"), Money(7, "USD")]
    assert sorted(wallet) == [Money(2, "USD"), Money(7, "USD"), Money(10, "USD")]
    assert max(wallet) == Money(10, "USD")


def test_money_compare_different_currencies_fails():
    with pytest.raises(ValueError):
        Money(1, "USD") < Money(2, "EUR")


def test_money_addition_returns_new_object():
    first = Money(5, "USD")
    total = first + Money(2.5, "USD")
    assert total == Money(7.5, "USD")
    assert first == Money(5, "USD")


def test_money_addition_different_currencies_fails():
    with pytest.raises(ValueError):
        Money(1, "USD") + Money(1, "GBP")


def test_deck_len_and_repr():
    deck = Deck(["AS", "KH", "QD"])
    assert len(deck) == 3
    assert repr(deck) == "Deck(3 cards)"


def test_deck_copies_its_cards():
    cards = ["AS", "KH"]
    deck = Deck(cards)
    deck.draw()
    assert cards == ["AS", "KH"]


def test_deck_draw_takes_last_card():
    deck = Deck(["AS", "KH"])
    assert deck.draw() == "KH"
    assert len(deck) == 1


def test_deck_empty():
    deck = Deck([])
    assert len(deck) == 0
    assert not deck
    with pytest.raises(IndexError):
        deck.draw()

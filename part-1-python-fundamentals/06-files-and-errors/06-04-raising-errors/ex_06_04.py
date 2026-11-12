"""Exercises for 06-04 Raising errors and validating input."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""


def validate_age(age):
    """Return `age` if it is a valid age, otherwise raise:
    - TypeError if `age` is not an int (use isinstance),
    - ValueError if it is below 0 or above 150.

    Example: validate_age(30) returns 30
    Example: validate_age(-1) raises ValueError
    """
    raise NotImplementedError


def parse_quantity(text):
    """Convert `text` (which may have spaces around it) to an int and
    return it. Raise ValueError if it is not a whole number, or if it is
    zero or negative. Include the bad text in the message.

    Example: parse_quantity(" 3 ") returns 3
    Example: parse_quantity("2.5") raises ValueError
    """
    raise NotImplementedError


def withdraw(balance, amount):
    """Return the balance after taking out `amount`.
    Raise ValueError if `amount` is zero or negative.
    Raise InsufficientFundsError (defined above) if `amount` is larger
    than `balance`.

    Example: withdraw(100, 30) returns 70
    """
    raise NotImplementedError


def require_fields(record, fields):
    """Raise KeyError if any name in the list `fields` is not a key of the
    dictionary `record`. The message must list the missing names in
    sorted order, separated by ", ". Return None if all are present.

    Example: require_fields({"name": "Ada"}, ["name", "email", "age"])
    raises KeyError with a message containing "age, email"
    """
    raise NotImplementedError

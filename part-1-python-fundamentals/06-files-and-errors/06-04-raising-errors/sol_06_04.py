"""Solutions for 06-04 Raising errors and validating input."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""


def validate_age(age):
    """Return `age` if valid, otherwise raise TypeError or ValueError."""
    # bool is a kind of int in Python, so reject it explicitly.
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError(f"age must be an int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be between 0 and 150, got {age}")
    return age


def parse_quantity(text):
    """Convert text to a positive int, or raise ValueError."""
    try:
        quantity = int(text)
    except ValueError:
        raise ValueError(f"quantity must be a whole number, got {text!r}")
    if quantity <= 0:
        raise ValueError(f"quantity must be positive, got {text!r}")
    return quantity


def withdraw(balance, amount):
    """Return the balance after a withdrawal."""
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    if amount > balance:
        raise InsufficientFundsError(f"balance {balance} is less than {amount}")
    return balance - amount


def require_fields(record, fields):
    """Raise KeyError listing any required fields missing from `record`."""
    missing = sorted(set(fields) - set(record))
    if missing:
        raise KeyError(f"missing fields: {', '.join(missing)}")

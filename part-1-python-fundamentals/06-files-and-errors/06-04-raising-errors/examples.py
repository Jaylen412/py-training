# 06-04 Raising errors and validating input


# Example 1: raise an exception when an argument makes no sense
def set_age(age):
    if age < 0:
        raise ValueError(f"age cannot be negative, got {age}")
    return age


print(set_age(30))
try:
    set_age(-5)
except ValueError as error:
    print("Caught:", error)


# Example 2: choosing the exception type
def average(numbers):
    if not isinstance(numbers, list):
        raise TypeError(f"expected a list, got {type(numbers).__name__}")
    if len(numbers) == 0:
        raise ValueError("cannot average an empty list")
    return sum(numbers) / len(numbers)


for argument in [[1, 2, 3], [], "123"]:
    try:
        print(average(argument))
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")


# Example 3: fail early - check everything at the top, then do the work
def make_order(item, quantity, unit_price):
    if not item.strip():
        raise ValueError("item name must not be empty")
    if quantity <= 0:
        raise ValueError(f"quantity must be positive, got {quantity}")
    if unit_price < 0:
        raise ValueError(f"unit price cannot be negative, got {unit_price}")
    return {"item": item.strip(), "quantity": quantity, "total": quantity * unit_price}


print(make_order(" pens ", 3, 1.5))


# Example 4: parse and validate text input in one place
def parse_amount(text):
    try:
        amount = float(text)
    except ValueError:
        raise ValueError(f"not a number: {text!r}")
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    return round(amount, 2)


for text in ["12.499", "abc", "-3"]:
    try:
        print("Amount:", parse_amount(text))
    except ValueError as error:
        print("Rejected:", error)


# Example 5: a custom exception class
class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"balance {balance} is less than {amount}")
    return balance - amount


print(withdraw(100, 30))
try:
    withdraw(100, 300)
except InsufficientFundsError as error:
    print("Declined:", error)

# Example 6: a custom exception is still an Exception
print(issubclass(InsufficientFundsError, Exception))

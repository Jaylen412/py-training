# 06-03 Exceptions
from pathlib import Path

# Example 1: try and except catch an error instead of crashing
try:
    result = 10 / 0
except ZeroDivisionError:
    result = None
print("Result:", result)

# Example 2: catching a specific exception from conversion
for text in ["42", "forty-two", "7"]:
    try:
        number = int(text)
        print("Converted", number)
    except ValueError:
        print("Could not convert", text)

# Example 3: the exception object holds the message
try:
    int("abc")
except ValueError as error:
    print("Error message:", error)
    print("Error type:", type(error).__name__)

# Example 4: several except blocks, checked in order
def safe_lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return "missing key"
    except IndexError:
        return "index out of range"
    except TypeError:
        return "wrong kind of key"


print(safe_lookup({"a": 1}, "b"))
print(safe_lookup([1, 2], 5))
print(safe_lookup([1, 2], "x"))

# Example 5: else runs only when no exception happened
try:
    value = int("12")
except ValueError:
    print("Not a number")
else:
    print("Doubled:", value * 2)

# Example 6: finally always runs
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        print(f"divide({a}, {b}) finished")


print(divide(6, 3))
print(divide(6, 0))

# Example 7: handling a missing file
missing = Path(__file__).parent / "does_not_exist.txt"
try:
    with open(missing) as file:
        content = file.read()
except FileNotFoundError:
    content = ""
    print("No file yet; starting empty")
print(repr(content))

# Example 8: keep the try block small - only the line that can fail
user_inputs = ["3", "x", "5"]
total = 0
bad_inputs = []
for text in user_inputs:
    try:
        number = int(text)
    except ValueError:
        bad_inputs.append(text)
        continue
    total += number
print("Total:", total, "Skipped:", bad_inputs)

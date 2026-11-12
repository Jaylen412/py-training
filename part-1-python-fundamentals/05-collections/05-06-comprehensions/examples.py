# 05-06 Comprehensions

# Example 1: the loop way and the comprehension way
squares = []
for number in range(1, 6):
    squares.append(number ** 2)
print(squares)

squares = [number ** 2 for number in range(1, 6)]
print(squares)

# Example 2: transforming each item
names = ["ada", "alan", "grace"]
print([name.title() for name in names])
print([len(name) for name in names])

# Example 3: filtering with if
numbers = [5, -2, 8, 0, -7, 3]
print([number for number in numbers if number > 0])
print([number * 10 for number in numbers if number % 2 == 0])

# Example 4: choosing a value with a conditional expression
print(["even" if number % 2 == 0 else "odd" for number in numbers])

# Example 5: dictionary comprehensions
print({name: len(name) for name in names})
prices = {"apple": 0.5, "bread": 1.2, "milk": 0.9}
print({item: round(price * 1.2, 2) for item, price in prices.items()})
print({item: price for item, price in prices.items() if price > 0.6})

# Example 6: set comprehensions
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
print(sorted({word[0] for word in words}))

# Example 7: two for clauses - flattening a grid
grid = [[1, 2, 3], [4, 5, 6]]
print([value for row in grid for value in row])

# Example 8: functions like sum, max and any accept a comprehension's items
print(sum([number ** 2 for number in range(1, 6)]))
print(max([len(word) for word in words]))
print(any([number < 0 for number in numbers]))
print(all([len(word) > 4 for word in words]))

# Example 9: when a plain loop is clearer - several steps per item
report = []
for word in words:
    first_letter = word[0].upper()
    length = len(word)
    if length > 5:
        report.append(f"{first_letter}: {word} ({length})")
print(report)

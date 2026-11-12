# 05-01 Lists

# Example 1: creating lists
scores = [72, 95, 88, 61]
names = ["Ada", "Grace", "Alan"]
mixed = [1, "two", 3.0, True]
empty = []
print(scores)
print(len(scores), len(empty))

# Example 2: indexing and slicing work like strings
print(scores[0], scores[-1])
print(scores[1:3])
print(names[::-1])

# Example 3: lists are mutable - change an item in place
scores[0] = 75
print(scores)

# Example 4: adding items
scores.append(80)
print(scores)
scores.extend([90, 55])
print(scores)
scores.insert(1, 100)
print(scores)

# Example 5: removing items
last = scores.pop()
print("Popped:", last, "->", scores)
first = scores.pop(0)
print("Popped:", first, "->", scores)
scores.remove(100)
print("Removed 100 ->", scores)

# Example 6: membership and searching
print(88 in scores)
print(scores.index(88))
print(scores.count(90))

# Example 7: built-in functions that work on lists
print(sum(scores), min(scores), max(scores))
print(sum(scores) / len(scores))

# Example 8: sort() changes the list; sorted() returns a new one
numbers = [3, 1, 2]
result = numbers.sort()
print(numbers, result)
letters = ["c", "a", "b"]
ordered = sorted(letters)
print(letters, ordered)
print(sorted(scores, reverse=True))

# Example 9: looping over a list and building a new one
prices = [4.99, 12.50, 3.25]
with_tax = []
for price in prices:
    with_tax.append(round(price * 1.2, 2))
print(with_tax)

# Example 10: list() turns other sequences into lists
print(list("abc"))
print(list(range(5)))

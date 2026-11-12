# 05-02 Tuples and unpacking

# Example 1: creating tuples
point = (3, 4)
colour = ("red", 255, 0, 0)
single = (42,)
print(point, colour, single)
print(type(point), len(colour))

# Example 2: indexing works; changing does not
print(point[0], colour[-1])
# point[0] = 10 would raise TypeError: tuples are immutable

# Example 3: packing - the brackets are optional
packed = 1, 2, 3
print(packed)

# Example 4: unpacking into separate variables
x, y = point
print("x is", x, "and y is", y)
name, red, green, blue = colour
print(name, red, green, blue)

# Example 5: swapping two variables
left = "L"
right = "R"
left, right = right, left
print(left, right)


# Example 6: returning several values from a function
def min_and_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = min_and_max([7, 2, 9, 4])
print(lowest, highest)
print(min_and_max([7, 2, 9, 4]))

# Example 7: star unpacking collects the rest into a list
first, *rest = [10, 20, 30, 40]
print(first, rest)

# Example 8: zip pairs up items from several sequences
names = ["Ada", "Grace", "Alan"]
scores = [95, 88, 72]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
print(list(zip(names, scores)))

# Example 9: zip stops at the shortest sequence
print(list(zip([1, 2, 3], ["a", "b"])))

# Example 10: a list of tuples, unpacked in a loop
students = [("Ada", 36), ("Alan", 41)]
for name, age in students:
    print(name, "is", age)

# Example 11: enumerate gives (index, item) tuples
print(list(enumerate(["x", "y"])))

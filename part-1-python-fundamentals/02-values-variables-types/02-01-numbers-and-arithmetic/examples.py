# 02-01 Numbers and arithmetic

# Example 1: two kinds of number
print(7)
print(7.0)
print(type(7))
print(type(7.0))

# Example 2: the basic operators
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)

# Example 3: floor division and remainder
print(7 // 2)
print(7 % 2)
print(135 // 60, "hours and", 135 % 60, "minutes")

# Example 4: powers
print(2 ** 10)
print(9 ** 0.5)

# Example 5: mixing int and float gives a float
print(3 + 1.5)
print(10 / 5)

# Example 6: operator precedence
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 * 3 ** 2)
print(-2 ** 2)
print((-2) ** 2)

# Example 7: float rounding surprises
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2))
print(round(3.14159, 3))
print(round(2.5), round(3.5))

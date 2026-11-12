# 13-01 Arrays
import numpy as np

# Example 1: an array from a list
prices = np.array([4.99, 12.50, 3.25, 8.00])
print(prices)
print(type(prices).__name__)

# Example 2: arrays do maths on every element; lists do not
price_list = [4.99, 12.50, 3.25, 8.00]
print(price_list * 2)
print(prices * 2)

# Example 3: dtype - every element has the same type
print(prices.dtype)
counts = np.array([3, 1, 4])
print(counts.dtype)
mixed = np.array([1, 2.5, 3])
print(mixed, mixed.dtype)
as_int = np.array([1.9, 2.1, -3.7]).astype(int)
print(as_int)

# Example 4: shape and ndim - one and two dimensions
table = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print(table)
print("shape:", table.shape, "ndim:", table.ndim, "size:", table.size)
print("shape:", prices.shape, "ndim:", prices.ndim)

# Example 5: arange and linspace
print(np.arange(5))
print(np.arange(2, 10, 3))
print(np.arange(0, 1, 0.25))
print(np.linspace(0, 1, 5))

# Example 6: zeros, ones and full
print(np.zeros(3))
print(np.ones((2, 4)))
print(np.full((2, 2), 7))
print(np.zeros(3, dtype=int))

# Example 7: back to Python lists
print(table.tolist())
print(prices.tolist()[0], type(prices[0]).__name__)

# 13-02 Indexing and slicing
import numpy as np

# Example 1: 1-D indexing and slicing work like lists
temperatures = np.array([12, 15, 9, 21, 18, 7, 14])
print(temperatures[0], temperatures[-1])
print(temperatures[2:5])
print(temperatures[::2])

# Example 2: 2-D indexing - [row, column]
scores = np.array([
    [72, 88, 95],   # student 0: maths, science, art
    [64, 70, 81],   # student 1
    [91, 85, 78],   # student 2
    [55, 62, 90],   # student 3
])
print(scores[1, 2])
print(scores[0])
print(scores[:, 0])
print(scores[1:3, :2])

# Example 3: slices are VIEWS - they share memory with the original
first_row = scores[0]
first_row[0] = 100
print(scores[0])
safe_copy = scores[0].copy()
safe_copy[0] = 0
print(scores[0], safe_copy)

# Example 4: boolean masks - select elements by a condition
warm = temperatures > 13
print(warm)
print(temperatures[warm])
print(temperatures[(temperatures > 10) & (temperatures < 20)])
print(temperatures[(temperatures < 8) | (temperatures > 20)])

# Example 5: counting and assigning with masks
print((temperatures > 13).sum())
adjusted = temperatures.copy()
adjusted[adjusted < 10] = 10
print(adjusted)

# Example 6: masks on rows of a 2-D array
passed_art = scores[:, 2] >= 80
print(passed_art)
print(scores[passed_art])

# Example 7: fancy indexing - a list of positions
print(temperatures[[0, 3, 6]])
print(scores[[3, 0]])
print(scores[:, [2, 0]])

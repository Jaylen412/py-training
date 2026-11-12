# Module 13: NumPy

The foundation of numerical Python. You will create arrays, select data with slices and boolean masks, compute on whole arrays at once with vectorised operations and broadcasting, summarise along axes, and use seeded random numbers and the dot product, the arithmetic behind linear models.

**Prerequisites:** Parts 1 and 2 (especially Module 12).

## Lessons

1. [13-01 Arrays](13-01-arrays/lesson.md)
2. [13-02 Indexing and slicing](13-02-indexing-and-slicing/lesson.md)
3. [13-03 Vectorised operations and broadcasting](13-03-vectorised-operations-and-broadcasting/lesson.md)
4. [13-04 Aggregations and axes](13-04-aggregations-and-axes/lesson.md)
5. [13-05 Random numbers and linear algebra basics](13-05-random-numbers-and-linear-algebra/lesson.md)

## Checkpoint quiz

1. What is `np.array([1, 2.5, 3]).dtype`, and why?
2. For a 2-D array `data`, how do you select the rows where column 2 is greater than 50?
3. Can shapes `(5, 3)` and `(5,)` be broadcast together? How would you subtract a per-row value?
4. For `data` with shape `(100, 4)`, what shape does `data.mean(axis=0)` have, and what does it mean?
5. What does `X @ w` compute when `X` has shape `(100, 4)` and `w` has shape `(4,)`?

<details>
<summary>Answers</summary>

1. `float64`. All elements of an array share one type, so the ints are upcast to floats.
2. `data[data[:, 2] > 50]`.
3. No: comparing from the right, 3 and 5 differ and neither is 1. Reshape the per-row values to a column: `data - values.reshape(-1, 1)`.
4. `(4,)`: the mean of each of the four columns (features).
5. 100 numbers: the dot product of each row with `w`, which is a linear model's prediction for each of the 100 examples.

</details>

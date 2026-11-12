# Module 17: Linear Algebra

The language of data and models. You will treat samples as vectors and datasets as matrices, measure lengths, distances and similarity with the dot product, multiply matrices with confidence about shapes, and see that a linear model is just **X** @ **w** + b, whose best weights come from solving equations.

**Prerequisites:** Parts 1 to 3 (especially Module 13).

## Lessons

1. [17-01 Vectors](17-01-vectors/lesson.md)
2. [17-02 Dot product and similarity](17-02-dot-product-and-similarity/lesson.md)
3. [17-03 Matrices](17-03-matrices/lesson.md)
4. [17-04 Linear models as matrix maths](17-04-linear-models-as-matrix-maths/lesson.md)

## Checkpoint quiz

1. What is the length of the vector (2, 3, 6)?
2. Two document vectors have cosine similarity 0.98 but a large Euclidean distance. What does that suggest?
3. What is the shape of `X @ W` if `X` is 200 × 5 and `W` is 5 × 3? Can you compute `W @ X`?
4. Why add a column of ones to **X**?
5. When would you use `np.linalg.lstsq` rather than `np.linalg.solve`?

<details>
<summary>Answers</summary>

1. 7: the square root of 4 + 9 + 36 = 49.
2. They point in almost the same direction (similar topic and word proportions) but have very different lengths (one document is much longer).
3. 200 × 3. `W @ X` would be (5 × 3) @ (200 × 5): the inner sizes 3 and 200 differ, so no.
4. So the bias becomes one of the weights, and the whole model is the single product **X** @ **w**.
5. When there are more equations (samples) than unknowns and no exact solution, as with noisy data; `solve` needs a square system with a unique solution.

</details>

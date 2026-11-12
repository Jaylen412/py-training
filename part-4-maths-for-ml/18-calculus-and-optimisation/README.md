# Module 18: Calculus and Optimisation

How models learn. You will meet derivatives as slopes, gradients as the direction of steepest increase, loss functions that score a model, and gradient descent, the algorithm that walks downhill on the loss to find good parameters. Everything is computed in NumPy; no algebra is required.

**Prerequisites:** Parts 1 to 3, and Module 17.

## Lessons

1. [18-01 Functions, slopes and derivatives](18-01-functions-slopes-and-derivatives/lesson.md)
2. [18-02 Gradients](18-02-gradients/lesson.md)
3. [18-03 Loss functions](18-03-loss-functions/lesson.md)
4. [18-04 Gradient descent](18-04-gradient-descent/lesson.md)

## Checkpoint quiz

1. The derivative of a function at x = 2 is −5. Which way should you move x to make the function smaller?
2. What does the gradient of a function of several variables tell you?
3. Why do we square residuals (or take absolute values) rather than just adding them?
4. Write the gradient descent update rule in words.
5. Your training loss goes 100, 400, 1600, 6400. What is wrong, and what do you change?

<details>
<summary>Answers</summary>

1. Increase x (move right): a negative derivative means the function decreases as x increases.
2. The rate of change along each input; together they give the direction of steepest increase. Its negative points straight downhill.
3. Positive and negative residuals cancel when summed, so a bad model could score zero.
4. New parameter equals old parameter minus the learning rate times the derivative (gradient) of the loss.
5. Training is diverging because the learning rate is too large. Reduce it (and check the features are on similar scales).

</details>

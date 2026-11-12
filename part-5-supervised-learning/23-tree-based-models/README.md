# Module 23: Tree-Based Models

From a single flowchart of questions to the strongest models for tabular data. You will build decision trees and see how they split and why they overfit, combine many trees into random forests, and build trees in sequence with gradient boosting.

**Prerequisites:** Parts 1 to 4, and Modules 20 to 22.

## Lessons

1. [23-01 Decision trees](23-01-decision-trees/lesson.md)
2. [23-02 Random forests](23-02-random-forests/lesson.md)
3. [23-03 Gradient boosting](23-03-gradient-boosting/lesson.md)

## Checkpoint quiz

1. A group contains 8 samples of class A and 2 of class B. What is its Gini impurity?
2. Why does an unlimited decision tree score 100% on its training data?
3. What two sources of randomness make the trees in a random forest different from each other?
4. Why can feature importances from a forest be misleading?
5. How does gradient boosting differ from a random forest, and why does it need early stopping?

<details>
<summary>Answers</summary>

1. 1 − (0.8² + 0.2²) = 1 − 0.68 = 0.32.
2. It keeps splitting until every leaf is pure, which can mean one training sample per leaf: it memorises the training set.
3. Each tree is trained on a bootstrap sample of the rows, and each split may only consider a random subset of the features.
4. They describe what the model used on the training data, not causes; correlated features share the credit; and even random noise receives some importance.
5. Boosting builds shallow trees in sequence, each correcting the errors of the ones before, rather than averaging independent deep trees. Because each tree keeps fitting what is left, adding too many eventually fits the noise, so early stopping halts training when validation performance stops improving.

</details>

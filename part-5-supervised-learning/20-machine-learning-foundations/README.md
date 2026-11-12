# Module 20: Machine Learning Foundations

What machine learning is, and how to evaluate it honestly. You will learn the vocabulary of supervised learning, use scikit-learn's consistent `fit`/`predict`/`score` interface, split data into training and test sets without leaking information, diagnose overfitting and underfitting, and compare every model against a baseline.

**Prerequisites:** Parts 1 to 4.

## Lessons

1. [20-01 What machine learning is](20-01-what-machine-learning-is/lesson.md) (concept)
2. [20-02 The scikit-learn interface](20-02-the-scikit-learn-interface/lesson.md)
3. [20-03 Train and test splits](20-03-train-and-test-splits/lesson.md)
4. [20-04 Overfitting and underfitting](20-04-overfitting-and-underfitting/lesson.md)
5. [20-05 Baselines](20-05-baselines/lesson.md)

## Checkpoint quiz

1. Is predicting whether a loan will be repaid regression or classification? Predicting how much of it will be repaid?
2. What shapes must X and y have in scikit-learn?
3. Why should you never fit a scaler on the full dataset before splitting?
4. A model scores 0.99 on training data and 0.81 on test data. What is happening, and name two things that might help.
5. A fraud model is 98% accurate and 98% of transactions are genuine. What would you say about it?

<details>
<summary>Answers</summary>

1. Classification (repaid or not). Regression (an amount).
2. X is 2-D with shape (samples, features); y is 1-D with shape (samples,).
3. The scaler's statistics would include information from the test set, which leaks into training and makes the test score optimistic. Fit it on the training data only.
4. Overfitting. A simpler model (or stronger regularisation), or more training data.
5. That it is no better than a baseline that always predicts "genuine". Accuracy is misleading here; look at how many fraudulent transactions it actually catches (Module 22).

</details>

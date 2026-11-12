# 20-01 What machine learning is

## What you will learn

- Explain the difference between writing rules and learning them from examples.
- Name the parts of a supervised learning problem: samples, features and targets.
- Distinguish supervised, unsupervised and reinforcement learning.
- Tell a regression problem from a classification problem.

## Why it matters

Everything so far has prepared for this: Python, data handling, and the maths of models. Part 5 is where models start making predictions. This lesson gives you the vocabulary used in every library, paper and job description, and a clear picture of what "learning" actually means: finding parameters from data, exactly as your gradient descent model did in the Part 4 project.

## Concepts

### Rules versus learning

Traditional programming means writing the rules yourself. Here is a hand-written rule for telling the three species of iris apart, by someone who has studied the flowers:

```python
def rule_based(row):
    if row["petal length (cm)"] < 2.5:
        return 0          # setosa
    if row["petal width (cm)"] < 1.75:
        return 1          # versicolor
    return 2              # virginica


rule_predictions = X.apply(rule_based, axis=1)
print("hand-written rule accuracy:", round((rule_predictions == y).mean(), 3))
```

```
hand-written rule accuracy: 0.96
```

(`X.apply(function, axis=1)` calls the function once per row.) The rule is right for 96% of the flowers. But someone had to study the data to write it, and for most problems (spotting spam, reading handwriting, predicting house prices) nobody can write the rules down.

**Machine learning** turns this around: you give a program **examples with the right answers**, and it works out the rules itself. A decision tree (Module 23) learns rules of exactly this "if feature < threshold" shape:

```python
model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)
print("learned rule accuracy:", round(model.score(X, y), 3))
```

```
learned rule accuracy: 0.96
```

It found an equally good rule on its own, from the 150 labelled examples. `fit` is the learning step; you met this interface in 09-05.

### Samples, features and targets

The vocabulary of a **supervised learning** problem:

- A **sample** (or example, instance, observation) is one thing we know about: one flower, one patient, one house. Each is a row.
- A **feature** (or input, variable, predictor) is something measured about each sample: petal length, age, floor area. Each is a column. The table of features is called **X**.
- The **target** (or label, output, response) is what we want to predict: the species, the disease progression, the price. The column of targets is called **y**.

```python
print(X.shape, y.shape)
print(X.columns.tolist())
print(iris.target_names.tolist())
print(X.iloc[0].tolist(), "->", int(y.iloc[0]))
```

```
(150, 4) (150,)
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
['setosa', 'versicolor', 'virginica']
[5.1, 3.5, 1.4, 0.2] -> 0
```

150 samples, 4 features, and one target per sample. The first flower's measurements map to class 0, setosa. A model is a function from features to target; **training** (or fitting) chooses its parameters so that it maps the training examples' features to their known targets as well as possible.

### Three kinds of machine learning

- **Supervised learning**: the training data includes the right answers (the targets). The model learns to map features to targets, so it can predict the target for new samples. This is Part 5: predicting species, prices, diagnoses.
- **Unsupervised learning**: there are no targets. The model looks for structure in the features alone: groups of similar customers, or a simpler way to describe the data. This is Part 6.
- **Reinforcement learning**: an agent learns by acting in an environment and receiving rewards or penalties, like a program learning to play a game by trial and error. It is a different field with its own methods, and is not covered in this course.

### Regression versus classification

Supervised learning splits by what kind of target you predict:

- **Classification**: the target is a **category** from a fixed set. Iris species, spam or not spam, malignant or benign. A classification with two classes is called **binary**; with more, **multi-class**.
- **Regression**: the target is a **number** on a continuous scale. House price, temperature, disease progression.

```python
print(np.unique(y))
diabetes = load_diabetes()
print(diabetes.target[:5])
```

```
[0 1 2]
[151.  75. 141. 206. 135.]
```

The iris target takes only three values, 0, 1 and 2, which stand for categories: classification. The diabetes target is a measurement that can be any number: regression. A quick test: does it make sense to say a prediction was "close"? Predicting 150 when the truth is 151 is close (regression); predicting class 1 when the truth is class 2 is just wrong (classification), even though the numbers are close.

### What learning cannot do

A model can only learn patterns that are in its training data. If the features carry no information about the target, no algorithm can predict it. If the training data is biased or unrepresentative, so is the model. And a model that is right on its training data may still be wrong on new data, the central problem of the rest of this module (20-03, 20-04).

## Common mistakes

- **Treating class numbers as quantities.** Iris classes 0, 1 and 2 are labels, not amounts: virginica is not "twice" versicolor. A regression model on these numbers would be meaningless.
- **Assuming more features always help.** Features unrelated to the target add noise and can make models worse.
- **Calling every prediction problem "AI".** Many problems are better solved by a simple rule or a straightforward calculation. Machine learning helps when the rules are too complex to write by hand and examples are available.

## Try it

For each of these, decide whether it is supervised or unsupervised, and if supervised, regression or classification: (a) predicting tomorrow's electricity demand; (b) grouping news articles by topic with no labels; (c) deciding whether a bank transaction is fraudulent from past labelled cases; (d) estimating a car's resale value.

## Summary

- Machine learning learns rules from examples instead of having them written by hand.
- Samples are rows, features are columns (**X**), the target is what we predict (**y**).
- Supervised learning has targets; unsupervised learning finds structure without them; reinforcement learning learns from rewards.
- Classification predicts a category; regression predicts a number.
- A model can only learn what its training data contains.

## Review questions

1. What does a supervised learning model need that an unsupervised one does not?
2. In a dataset of 1,000 houses with 12 measurements each and a sale price, what are the shapes of **X** and **y**?
3. Is predicting a customer's star rating (1 to 5 stars) regression or classification? Can it be argued both ways?
4. Why is high accuracy on the training data not enough to trust a model?
5. Give one example of a problem where writing rules by hand would be better than machine learning.

<details>
<summary>Answers</summary>

1. Targets: the right answer for each training sample.
2. **X** is (1000, 12) and **y** is (1000,).
3. Either. As classification, the five ratings are separate categories. As regression, they are ordered numbers, and predicting 4 for a true 5 is "closer" than predicting 1. The choice depends on what kinds of mistakes matter.
4. The model may have memorised the training examples, including their noise, and perform much worse on new data. It must be tested on data it has not seen (20-03).
5. Any well-defined calculation, such as working out sales tax or checking whether a date is valid. The rules are known exactly, so there is nothing to learn, and a learned model could only add errors.

</details>

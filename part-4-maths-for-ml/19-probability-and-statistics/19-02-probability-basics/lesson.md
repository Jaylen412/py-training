# 19-02 Probability basics

## What you will learn

- Compute probabilities by counting outcomes, and estimate them by simulation.
- Calculate conditional probabilities from data.
- Test whether two events are independent.
- Use Bayes' rule, and explain why a positive test for a rare disease is often wrong.

## Why it matters

Classifiers output probabilities ("this email is 92% likely to be spam"), and the Naive Bayes classifier in Module 22 is Bayes' rule applied to data. More importantly, probability protects you from a very common error: confusing "the chance of a positive test if you are ill" with "the chance you are ill if you test positive". These can differ enormously, and the same mistake appears when reading a model's precision and recall (Module 22).

## Concepts

### Probability as counting

The **probability** of an **event** is a number from 0 (impossible) to 1 (certain). When all outcomes are equally likely, it is the fraction of outcomes in which the event happens. For a fair die, "even" happens in 3 of 6 outcomes:

```python
dice = np.arange(1, 7)
print((dice % 2 == 0).mean())
print((dice >= 5).mean())
```

```
0.5
0.3333333333333333
```

The mean of a boolean array is the fraction of `True` values, which makes it a convenient way to count. P(A) is the usual shorthand for "the probability of event A".

### Probability by simulation

When counting is hard, simulate: generate many random outcomes and count how often the event happens. The more trials, the closer the estimate:

```python
rng = np.random.default_rng(42)
rolls = rng.integers(1, 7, size=100_000)
print(round((rolls >= 5).mean(), 4))
first = rng.integers(1, 7, size=100_000)
second = rng.integers(1, 7, size=100_000)
print(round(((first + second) == 7).mean(), 4), round(1 / 6, 4))
```

```
0.334
0.164 0.1667
```

A total of 7 with two dice happens in 6 of the 36 equally likely pairs, 1/6; the simulation gives 0.164.

### Probabilities from data

In a dataset, the probability of an event is estimated by the fraction of rows where it happens. In the breast cancer data (16-01):

```python
data = load_breast_cancer(as_frame=True).frame
malignant = data["target"] == 0
large = data["mean radius"] > 15
print(round(malignant.mean(), 3), round(large.mean(), 3))
print(round((malignant & large).mean(), 3))
```

```
0.373 0.304
0.283
```

37.3% of tumours are malignant, 30.4% are large (mean radius over 15), and 28.3% are both: P(malignant and large) = 0.283.

### Conditional probability

A **conditional probability** is the probability of one event **given** that another has happened, written P(A | B), "the probability of A given B". To compute it, restrict to the rows where B is true, then count A:

```python
print(round(malignant[large].mean(), 3))
print(round((malignant & large).mean() / large.mean(), 3))
print(round(malignant[~large].mean(), 3))
```

```
0.931
0.931
0.129
```

The formula P(A | B) = P(A and B) / P(B) gives the same answer. In words: of the cases where B happens, what fraction also have A? Knowing a tumour is large raises the probability of malignancy from 37.3% to 93.1%; for small tumours it is 12.9%. This is exactly why tumour size is a useful feature for a classifier.

A **contingency table** (also called a crosstab) shows the counts behind these numbers:

```python
print(pd.crosstab(large.rename("large"), malignant.rename("malignant"), margins=True))
```

```
malignant  False  True  All
large                      
False        345    51  396
True          12   161  173
All          357   212  569
```

161 of the 173 large tumours are malignant: 161 / 173 = 0.931.

### Independence

Two events are **independent** if knowing one tells you nothing about the other: P(A | B) = P(A), or equivalently P(A and B) = P(A) × P(B).

```python
coin = rng.integers(0, 2, size=100_000)
die = rng.integers(1, 7, size=100_000)
print(round((die == 6).mean(), 3), round((die[coin == 1] == 6).mean(), 3))
print(round(malignant.mean() * large.mean(), 3), round((malignant & large).mean(), 3))
```

```
0.167 0.169
0.113 0.283
```

A coin toss does not change the chance of a six: independent. But if size and malignancy were independent, we would expect 0.373 × 0.304 = 0.113 of tumours to be both; in fact 0.283 are. They are strongly **dependent**. Features that are dependent on the target are what make prediction possible.

### Bayes' rule

**Bayes' rule** turns one conditional probability around into the other:

P(A | B) = P(B | A) × P(A) / P(B)

In words: the probability of A given B equals the probability of B given A, times how common A is in the first place, divided by how common B is.

The classic example is a medical test. A disease affects 1% of people. The test catches 95% of people who have it (its **sensitivity**, P(positive | disease)), and wrongly flags 5% of healthy people (its **false positive rate**). You test positive. How likely is it that you have the disease?

```python
prevalence = 0.01          # 1% of people have the disease
sensitivity = 0.95         # P(positive | disease)
false_positive_rate = 0.05 # P(positive | no disease)
p_positive = sensitivity * prevalence + false_positive_rate * (1 - prevalence)
p_disease_given_positive = sensitivity * prevalence / p_positive
print(round(p_positive, 4), round(p_disease_given_positive, 4))
```

```
0.059 0.161
```

Only about **16%**. P(positive) adds up the two ways to test positive: being ill and caught, or being healthy and wrongly flagged. Even though the test is "95% accurate", most positives are false alarms, because healthy people vastly outnumber ill ones.

Simulating a population of a million people makes it concrete:

```python
population = 1_000_000
has_disease = rng.random(population) < prevalence
positive = np.where(has_disease, rng.random(population) < sensitivity,
                    rng.random(population) < false_positive_rate)
print(int(positive.sum()), int((positive & has_disease).sum()))
print(round(has_disease[positive].mean(), 4))
```

```
59141 9356
0.1582
```

`np.where(condition, a, b)` takes values from `a` where the condition is true and from `b` elsewhere. Of 59,141 positive tests, only 9,356 come from people who are ill. The starting probability, P(disease) = 1%, is called the **prior**; the updated probability after the evidence, 16%, is the **posterior**. Ignoring the prior is called the **base rate fallacy**.

## Common mistakes

- **Confusing P(A | B) with P(B | A).** P(positive | disease) = 95% is not P(disease | positive) = 16%.
- **Assuming independence.** Multiplying probabilities is only valid for independent events; size and malignancy are far from independent.
- **Ignoring the base rate.** Rare events produce many false alarms, even with accurate tests or models. You will see this again with imbalanced classes in Module 22.
- **Too few simulation trials.** 100 trials can be off by several percentage points. Use tens of thousands.

## Try it

Rerun the medical test calculation with prevalence 10%, then 50%. How does P(disease | positive) change? What false positive rate would be needed for a positive test to mean an 80% chance of disease when prevalence is 1%?

## Exercises

Open `ex_19_02.py`:

1. `probability`: the fraction of `True` values in a boolean array.
2. `conditional_probability`: P(A | B) from two boolean arrays.
3. `are_independent`: whether P(A and B) is close to P(A) × P(B).
4. `bayes_posterior`: P(disease | positive) from prevalence, sensitivity and false positive rate.
5. `simulate_two_dice`: estimate the probability of a total by simulation.

Run the tests:

```
python -m pytest part-4-maths-for-ml/19-probability-and-statistics/19-02-probability-basics
```

## Summary

- A probability is a number from 0 to 1; with equally likely outcomes it is a fraction of outcomes, and in data it is a fraction of rows.
- Simulation estimates probabilities by counting over many random trials.
- P(A | B) = P(A and B) / P(B): restrict to the rows where B is true.
- Independent events satisfy P(A and B) = P(A) × P(B); useful features are dependent on the target.
- Bayes' rule, P(A | B) = P(B | A) P(A) / P(B), combines evidence with the prior; ignoring the prior leads to the base rate fallacy.

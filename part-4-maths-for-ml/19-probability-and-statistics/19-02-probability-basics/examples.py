# 19-02 Probability basics
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Example 1: probability as a fraction of equally likely outcomes
dice = np.arange(1, 7)
print((dice % 2 == 0).mean())
print((dice >= 5).mean())

# Example 2: estimating a probability by simulation
rng = np.random.default_rng(42)
rolls = rng.integers(1, 7, size=100_000)
print(round((rolls >= 5).mean(), 4))

# Example 3: two dice - the probability the total is 7
first = rng.integers(1, 7, size=100_000)
second = rng.integers(1, 7, size=100_000)
print(round(((first + second) == 7).mean(), 4), round(1 / 6, 4))

# Example 4: probabilities from data - breast cancer tumours
data = load_breast_cancer(as_frame=True).frame
malignant = data["target"] == 0
large = data["mean radius"] > 15
print(round(malignant.mean(), 3), round(large.mean(), 3))
print(round((malignant & large).mean(), 3))

# Example 5: conditional probability - P(malignant | large)
print(round(malignant[large].mean(), 3))
print(round((malignant & large).mean() / large.mean(), 3))
print(round(malignant[~large].mean(), 3))

# Example 6: independence - does knowing one thing change the other?
coin = rng.integers(0, 2, size=100_000)
die = rng.integers(1, 7, size=100_000)
print(round((die == 6).mean(), 3), round((die[coin == 1] == 6).mean(), 3))
print(round(malignant.mean() * large.mean(), 3), round((malignant & large).mean(), 3))

# Example 7: a contingency table shows the same counts
print(pd.crosstab(large.rename("large"), malignant.rename("malignant"), margins=True))

# Example 8: Bayes' rule - a medical test
prevalence = 0.01          # 1% of people have the disease
sensitivity = 0.95         # P(positive | disease)
false_positive_rate = 0.05 # P(positive | no disease)
p_positive = sensitivity * prevalence + false_positive_rate * (1 - prevalence)
p_disease_given_positive = sensitivity * prevalence / p_positive
print(round(p_positive, 4), round(p_disease_given_positive, 4))

# Example 9: the same answer by simulating a population
population = 1_000_000
has_disease = rng.random(population) < prevalence
positive = np.where(has_disease, rng.random(population) < sensitivity,
                    rng.random(population) < false_positive_rate)
print(int(positive.sum()), int((positive & has_disease).sum()))
print(round(has_disease[positive].mean(), 4))

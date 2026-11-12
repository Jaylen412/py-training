# 22-05 Naive Bayes
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

pd.set_option("display.width", 120)

# Example 1: Bayes' rule for classification, by hand, with one feature
iris = load_iris()
petal_length = iris.data[:, 2]
classes = iris.target
priors = np.bincount(classes) / len(classes)
means = np.array([petal_length[classes == c].mean() for c in range(3)])
stds = np.array([petal_length[classes == c].std() for c in range(3)])
print(np.round(priors, 3), np.round(means, 3), np.round(stds, 3))


def normal_density(x, mean, std):
    return np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))


new_length = 4.9
likelihoods = normal_density(new_length, means, stds)
unnormalised = likelihoods * priors
posteriors = unnormalised / unnormalised.sum()
print(np.round(likelihoods, 4))
print(np.round(posteriors, 3), iris.target_names[posteriors.argmax()])

# Example 2: the same thing with GaussianNB
one_feature = GaussianNB().fit(petal_length.reshape(-1, 1), classes)
print(np.round(one_feature.predict_proba([[new_length]]), 3))
print(np.round(one_feature.theta_.ravel(), 3))

# Example 3: all features - multiply the likelihoods together (the naive assumption)
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42, stratify=iris.target
)
model = GaussianNB().fit(X_train, y_train)
print("test accuracy:", round(model.score(X_test, y_test), 3))
print(np.round(model.predict_proba(X_test[:3]), 3))

# Example 4: the independence assumption is usually false
print(np.round(np.corrcoef(iris.data[:, 2], iris.data[:, 3])[0, 1], 3))

# Example 5: it is fast and works well even so - wine data
wine = load_wine()
Xw_train, Xw_test, yw_train, yw_test = train_test_split(
    wine.data, wine.target, test_size=0.3, random_state=42, stratify=wine.target
)
print("wine test accuracy:", round(GaussianNB().fit(Xw_train, yw_train).score(Xw_test, yw_test), 3))

# Example 6: but its probabilities are often overconfident
probabilities = GaussianNB().fit(Xw_train, yw_train).predict_proba(Xw_test)
print("share of predictions with probability above 0.99:", round(np.mean(probabilities.max(axis=1) > 0.99), 3))

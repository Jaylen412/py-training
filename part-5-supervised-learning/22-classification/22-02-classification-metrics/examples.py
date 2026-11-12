# 22-02 Classification metrics
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score, classification_report,
                             confusion_matrix, f1_score, precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Malignant is the class we care about finding, so make it the "positive" class 1
cancer = load_breast_cancer()
y = (cancer.target == 0).astype(int)
X_train, X_test, y_train, y_test = train_test_split(cancer.data, y, test_size=0.25, random_state=42, stratify=y)
scaler = StandardScaler().fit(X_train)
model = LogisticRegression(max_iter=1000).fit(scaler.transform(X_train), y_train)
predictions = model.predict(scaler.transform(X_test))

# Example 1: the confusion matrix
matrix = confusion_matrix(y_test, predictions)
print(matrix)
tn, fp, fn, tp = matrix.ravel()
print(f"TN={tn} FP={fp} FN={fn} TP={tp}")

fig, ax = plt.subplots(figsize=(4.5, 4))
ConfusionMatrixDisplay(matrix, display_labels=["benign", "malignant"]).plot(ax=ax, colorbar=False)
ax.set_title("Confusion matrix (test set)")
fig.savefig(FIGURES / "confusion_matrix.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: accuracy, precision, recall and F1
print(round(accuracy_score(y_test, predictions), 3), round((tp + tn) / (tp + tn + fp + fn), 3))
print(round(precision_score(y_test, predictions), 3), round(tp / (tp + fp), 3))
print(round(recall_score(y_test, predictions), 3), round(tp / (tp + fn), 3))
print(round(f1_score(y_test, predictions), 3))

# Example 3: classification_report shows everything per class
print(classification_report(y_test, predictions, target_names=["benign", "malignant"], digits=3))

# Example 4: why accuracy misleads with imbalanced classes
X, y_rare = make_classification(n_samples=4000, weights=[0.97], flip_y=0, class_sep=0.8, random_state=42)
Xr_train, Xr_test, yr_train, yr_test = train_test_split(X, y_rare, test_size=0.25, random_state=42, stratify=y_rare)
for name, clf in [("always negative", DummyClassifier(strategy="most_frequent")),
                  ("logistic regression", LogisticRegression())]:
    pred = clf.fit(Xr_train, yr_train).predict(Xr_test)
    print(f"{name:<20} accuracy {accuracy_score(yr_test, pred):.3f}  "
          f"recall {recall_score(yr_test, pred, zero_division=0):.3f}  "
          f"precision {precision_score(yr_test, pred, zero_division=0):.3f}")
print(confusion_matrix(yr_test, LogisticRegression().fit(Xr_train, yr_train).predict(Xr_test)))

# Example 5: class_weight="balanced" pays more attention to the rare class
balanced = LogisticRegression(class_weight="balanced").fit(Xr_train, yr_train)
pred = balanced.predict(Xr_test)
print(f"balanced weights     accuracy {accuracy_score(yr_test, pred):.3f}  "
      f"recall {recall_score(yr_test, pred):.3f}  precision {precision_score(yr_test, pred):.3f}")

# 22-03 Thresholds, ROC and precision-recall curves
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (average_precision_score, precision_recall_curve, precision_score,
                             recall_score, roc_auc_score, roc_curve)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

cancer = load_breast_cancer()
y = (cancer.target == 0).astype(int)          # 1 = malignant
X_train, X_test, y_train, y_test = train_test_split(cancer.data, y, test_size=0.25, random_state=42, stratify=y)
scaler = StandardScaler().fit(X_train)
model = LogisticRegression(C=0.05, max_iter=1000).fit(scaler.transform(X_train), y_train)
probabilities = model.predict_proba(scaler.transform(X_test))[:, 1]

# Example 1: predict uses a threshold of 0.5
print(np.array_equal(model.predict(scaler.transform(X_test)), (probabilities >= 0.5).astype(int)))

# Example 2: moving the threshold trades precision for recall
for threshold in [0.1, 0.3, 0.5, 0.7, 0.9]:
    pred = (probabilities >= threshold).astype(int)
    print(f"threshold {threshold}: precision {precision_score(y_test, pred):.3f}, recall {recall_score(y_test, pred):.3f}, "
          f"flagged {pred.sum()}")

# Example 3: the ROC curve and its area
false_positive_rate, true_positive_rate, roc_thresholds = roc_curve(y_test, probabilities)
auc = roc_auc_score(y_test, probabilities)
print("ROC AUC:", round(auc, 4))

# Example 4: the precision-recall curve
precision, recall, pr_thresholds = precision_recall_curve(y_test, probabilities)
print("average precision:", round(average_precision_score(y_test, probabilities), 4))

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
axes[0].plot(false_positive_rate, true_positive_rate, label=f"logistic regression (AUC {auc:.3f})")
axes[0].plot([0, 1], [0, 1], "--", color="grey", label="random guessing (AUC 0.5)")
axes[0].set_xlabel("False positive rate")
axes[0].set_ylabel("True positive rate (recall)")
axes[0].set_title("ROC curve")
axes[0].legend(loc="lower right")
axes[1].plot(recall, precision)
axes[1].axhline(y_test.mean(), linestyle="--", color="grey", label="random guessing")
axes[1].set_xlabel("Recall")
axes[1].set_ylabel("Precision")
axes[1].set_title("Precision-recall curve")
axes[1].legend(loc="lower left")
fig.tight_layout()
fig.savefig(FIGURES / "roc_and_pr.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: choose the threshold with the lowest total cost
cost_of_missed_cancer = 20      # a false negative
cost_of_false_alarm = 1         # a false positive
thresholds = np.linspace(0.01, 0.99, 99)
costs = []
for threshold in thresholds:
    pred = probabilities >= threshold
    false_negatives = np.sum(~pred & (y_test == 1))
    false_positives = np.sum(pred & (y_test == 0))
    costs.append(cost_of_missed_cancer * false_negatives + cost_of_false_alarm * false_positives)
best = thresholds[int(np.argmin(costs))]
print("lowest-cost threshold:", round(best, 2), "cost:", min(costs))
print("cost at 0.5:", costs[49])

# Example 6: the smallest threshold that still gives at least 90% precision
precise_enough = pr_thresholds[precision[:-1] >= 0.9]
print("smallest threshold with precision >= 0.9:", round(precise_enough.min(), 3))

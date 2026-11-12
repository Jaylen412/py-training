# 19-01 Describing data
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

# Example 1: a small sample of exam scores
scores = np.array([62, 71, 71, 75, 78, 80, 84, 88, 95, 41])

# Example 2: measures of the centre
print(scores.mean(), np.median(scores))
values, counts = np.unique(scores, return_counts=True)
print(values[counts.argmax()])

# Example 3: the mean is pulled by extreme values; the median is not
with_outlier = np.append(scores, 400)
print(round(with_outlier.mean(), 2), np.median(with_outlier))

# Example 4: spread - variance and standard deviation
deviations = scores - scores.mean()
print(deviations)
variance = np.mean(deviations ** 2)
print(variance, np.var(scores))
print(round(np.sqrt(variance), 3), round(np.std(scores), 3))

# Example 5: sample variance divides by n - 1
print(round(np.var(scores, ddof=1), 3), round(np.std(scores, ddof=1), 3))
print(round(pd.Series(scores).std(), 3))

# Example 6: the range and percentiles
print(scores.min(), scores.max(), scores.max() - scores.min())
print(np.percentile(scores, [25, 50, 75]))
q1, q3 = np.percentile(scores, [25, 75])
print("IQR:", q3 - q1)

# Example 7: z-scores - how unusual is each value?
z = (scores - scores.mean()) / scores.std()
print(np.round(z, 2))
print(scores[np.abs(z) > 2])

# Example 8: a real dataset - body mass index of 442 diabetes patients
bmi = load_diabetes(as_frame=True, scaled=False).frame["bmi"]
print(len(bmi))
print(round(bmi.mean(), 2), bmi.median(), round(bmi.std(), 2))
print(bmi.quantile([0.1, 0.5, 0.9]).round(2).tolist())
print(round(bmi.skew(), 2))

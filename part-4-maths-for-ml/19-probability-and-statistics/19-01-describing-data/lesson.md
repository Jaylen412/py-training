# 19-01 Describing data

## What you will learn

- Measure the centre of data with the mean, median and mode.
- Measure spread with the variance, standard deviation, range and interquartile range.
- Explain the difference between population and sample variance.
- Use percentiles and z-scores to say how unusual a value is.

## Why it matters

Before any model, you summarise. These few numbers appear everywhere: `describe()` in pandas (14-01), standardising features (13-03), outlier rules (16-02), and every model evaluation. Knowing exactly what each one measures, and when it misleads, stops you drawing the wrong conclusion from a summary.

## Concepts

The examples use ten exam scores:

```python
scores = np.array([62, 71, 71, 75, 78, 80, 84, 88, 95, 41])
```

### The centre: mean, median, mode

- The **mean** (average) is the sum divided by the count.
- The **median** is the middle value after sorting (the average of the two middle values when there is an even number).
- The **mode** is the most common value.

```python
print(scores.mean(), np.median(scores))
values, counts = np.unique(scores, return_counts=True)
print(values[counts.argmax()])
```

```
74.5 76.5
71
```

`np.unique(..., return_counts=True)` returns the distinct values and how often each appears; the mode is the value with the largest count. The mode is most useful for categories ("the most common product").

### Mean versus median

The mean uses every value's size, so one extreme value can drag it a long way. The median only cares about order, so it barely moves. Add one score of 400 (a data-entry error):

```python
with_outlier = np.append(scores, 400)
print(round(with_outlier.mean(), 2), np.median(with_outlier))
```

```
104.09 78.0
```

The mean jumped from 74.5 to 104.09, higher than any real score; the median moved from 76.5 to 78. For skewed data such as incomes or house prices, the median is usually the better "typical" value. A mean much larger than the median signals a long right tail (16-02).

### Spread: variance and standard deviation

Two classes could have the same mean score but very different spreads. The **variance** measures spread as the average squared distance from the mean. The **standard deviation** (SD) is its square root, which puts it back in the original units:

```python
deviations = scores - scores.mean()
print(deviations)
variance = np.mean(deviations ** 2)
print(variance, np.var(scores))
print(round(np.sqrt(variance), 3), round(np.std(scores), 3))
```

```
[-12.5  -3.5  -3.5   0.5   3.5   5.5   9.5  13.5  20.5 -33.5]
203.85 203.85
14.278 14.278
```

In words: subtract the mean from each value, square, average, then take the square root. A typical score is about 14 points from the average. (This is the same calculation as the MSE in 18-03, with the mean as the "prediction".)

### Population versus sample

The **population** is everyone you care about; a **sample** is the part you actually measured. When the data is only a sample, dividing by n slightly **underestimates** the population's variance, because the sample's own mean is always a little closer to the sample's values than the true mean is. Dividing by **n − 1** instead corrects this. NumPy divides by n by default; pass `ddof=1` ("delta degrees of freedom") for the sample version. pandas uses n − 1 by default:

```python
print(round(np.var(scores, ddof=1), 3), round(np.std(scores, ddof=1), 3))
print(round(pd.Series(scores).std(), 3))
```

```
226.5 15.05
15.05
```

With large datasets the difference is negligible. With ten values it is about 5%. Just be aware that NumPy and pandas give slightly different answers by default.

### Range, percentiles and the IQR

The **range** is the maximum minus the minimum, but it depends entirely on the two most extreme values. **Percentiles** are more robust: the p-th percentile is the value below which p% of the data falls. The 25th, 50th and 75th percentiles are the **quartiles**, and the 50th is the median:

```python
print(scores.min(), scores.max(), scores.max() - scores.min())
print(np.percentile(scores, [25, 50, 75]))
q1, q3 = np.percentile(scores, [25, 75])
print("IQR:", q3 - q1)
```

```
41 95 54
[71.  76.5 83. ]
IQR: 12.0
```

The **interquartile range** (IQR), Q3 − Q1, is the spread of the middle half of the data, and it drives the outlier rule and box plots (15-02, 16-02).

### z-scores

A **z-score** expresses a value as a number of standard deviations from the mean: z = (x − mean) / SD. It answers "how unusual is this value?" in a way that works for any units:

```python
z = (scores - scores.mean()) / scores.std()
print(np.round(z, 2))
print(scores[np.abs(z) > 2])
```

```
[-0.88 -0.25 -0.25  0.04  0.25  0.39  0.67  0.95  1.44 -2.35]
[41]
```

The score of 41 is 2.35 standard deviations below the mean, much more unusual than the 95, which is 1.44 above. Converting every feature to z-scores is exactly standardising (13-03).

### A real dataset

The diabetes dataset from scikit-learn records body mass index (BMI) for 442 patients. `scaled=False` gives the original units:

```python
bmi = load_diabetes(as_frame=True, scaled=False).frame["bmi"]
print(len(bmi))
print(round(bmi.mean(), 2), bmi.median(), round(bmi.std(), 2))
print(bmi.quantile([0.1, 0.5, 0.9]).round(2).tolist())
print(round(bmi.skew(), 2))
```

```
442
26.38 25.7 4.42
[21.0, 25.7, 32.28]
0.6
```

Mean 26.4, median 25.7: a mild right skew (skew 0.6). 80% of patients have a BMI between 21.0 and 32.3.

## Common mistakes

- **Reporting the mean of skewed data alone.** Average income is dominated by the richest people. Report the median too.
- **Forgetting that NumPy and pandas differ.** `np.std` divides by n; `Series.std()` divides by n − 1. Pass `ddof` to be explicit.
- **Comparing standard deviations across different units.** An SD of 10 is huge for exam percentages and tiny for house prices. Use z-scores or relative measures.
- **Taking the mode of continuous data.** With measurements such as 26.38 and 26.41, almost every value is unique, so the mode is meaningless. Use a histogram instead.

## Try it

For the diabetes `target` (disease progression after a year), compute the mean, median, SD and quartiles. Is it skewed? Which patients have z-scores beyond ±2.5?

## Exercises

Open `ex_19_01.py`. Write `median` and `variance` without the NumPy functions of the same name, so you see the definitions at work.

1. `median`: the middle value.
2. `mode`: the most common value.
3. `variance`: population or sample variance.
4. `z_scores`: every value as a z-score.
5. `percentile_rank`: the percentage of values below a given value.

Run the tests:

```
python -m pytest part-4-maths-for-ml/19-probability-and-statistics/19-01-describing-data
```

## Summary

- Centre: the mean (sensitive to extremes), the median (robust) and the mode (most common).
- Spread: the variance is the average squared deviation; the standard deviation is its square root.
- Use n − 1 (`ddof=1`) for a sample estimate of a population's variance; NumPy and pandas differ by default.
- Percentiles and the IQR describe spread robustly; z-scores say how many SDs a value is from the mean.
- When the mean is well above the median, the data has a long right tail.

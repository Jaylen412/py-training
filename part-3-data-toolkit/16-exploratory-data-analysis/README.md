# Module 16: Exploratory Data Analysis

Bring Modules 13 to 15 together to get to know a dataset before modelling it. You will follow a repeatable EDA checklist, write findings backed by evidence, and learn to question patterns: outliers, skew, misleading correlations and Simpson's paradox.

**Prerequisites:** Parts 1 and 2, and Modules 13 to 15.

## Lessons

1. [16-01 An EDA workflow](16-01-an-eda-workflow/lesson.md)
2. [16-02 Outliers, skew and correlation](16-02-outliers-skew-and-correlation/lesson.md)

## Checkpoint quiz

1. List the seven steps of the EDA checklist.
2. Why does the class balance of the target matter before you build a model?
3. A column has mean 120 and median 40. What does that suggest, and what transform might help?
4. The IQR rule flags 50 rows as outliers. What should you do before removing them?
5. Ice-cream sales and drowning deaths are correlated. Does ice cream cause drowning? What is going on?

<details>
<summary>Answers</summary>

1. Shape; types; missing values and duplicates; the target; distributions; relationships; written findings.
2. With imbalanced classes, a model that always predicts the majority class can score a high accuracy while being useless, so evaluation must take the balance into account.
3. A strong right skew (a long tail of large values). A log transform such as `np.log1p` reduces it.
4. Inspect them: find out which rows they are and whether they are errors or real extreme values. Only fix or remove errors, and record what you did.
5. No. A confounder, hot weather, increases both ice-cream sales and swimming (and so drownings).

</details>

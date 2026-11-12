# Module 19: Probability and Statistics

Reason about data and uncertainty. You will summarise data with centre and spread, compute probabilities and use Bayes' rule, simulate the common distributions and see the central limit theorem at work, and measure relationships and the uncertainty of estimates with correlation and the bootstrap.

**Prerequisites:** Parts 1 to 3, and Modules 17 and 18.

## Lessons

1. [19-01 Describing data](19-01-describing-data/lesson.md)
2. [19-02 Probability basics](19-02-probability-basics/lesson.md)
3. [19-03 Distributions and sampling](19-03-distributions-and-sampling/lesson.md)
4. [19-04 Covariance, correlation and sampling error](19-04-covariance-correlation-and-sampling-error/lesson.md)

## Checkpoint quiz

1. When should you prefer the median to the mean?
2. A test is 99% sensitive with a 1% false positive rate, and the condition affects 1 in 1,000 people. Is a positive result likely to be correct?
3. What does the central limit theorem say about the means of large samples?
4. Why is correlation easier to interpret than covariance?
5. Describe the bootstrap in two sentences.

<details>
<summary>Answers</summary>

1. When the data is skewed or has outliers, because the median is not dragged by extreme values.
2. No. P(positive) is about 0.99 × 0.001 + 0.01 × 0.999 ≈ 0.011, so P(condition | positive) ≈ 0.00099 / 0.011 ≈ 9%. Most positives are false alarms because the condition is rare.
3. They are approximately normally distributed around the population mean, with standard error equal to the population SD divided by √n, whatever the shape of the population.
4. Correlation is divided by both standard deviations, so it has no units and always lies between −1 and 1.
5. Resample your data with replacement many times, computing the statistic each time. The spread of those results estimates the statistic's sampling error, and its middle 95% gives a confidence interval.

</details>

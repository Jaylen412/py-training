# Predicting customer churn

Fill in each section with your own numbers from `churn_model.py`. Keep it to a page or two.

## Problem and success measure

What are you predicting, who will use it, and how will you judge success? Decide the metric and the relative cost of each kind of mistake **before** you look at results.

## Data

How many rows, what share churned, where are the gaps, and what did the quick look at the data show (for example, churn by contract)?

## Method

How did you split the data, what does the pipeline do to each group of columns, how were models compared, what did you tune, and how did you choose the threshold?

## Results

A table of cross-validated ROC AUC for every candidate (including the baseline). Then the test-set metrics for your final model at the default and at your chosen threshold, and the evaluation figure from `figures/evaluation.png`.

## What matters

Which features had the strongest coefficients, and what do they say in plain language? Be careful to describe associations, not causes.

## What the model gets wrong

Who does it miss, and who does it flag wrongly? What does the threshold trade off in practice?

## Limitations

What could make these numbers too optimistic or too pessimistic? (Think about test-set size, assumed costs and the data itself.)

## What to try next

Two or three concrete next steps.

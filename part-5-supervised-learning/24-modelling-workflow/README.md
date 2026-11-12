# Module 24: The Modelling Workflow

Turn messy real data into a trustworthy model. You will encode categories and fill gaps, package preprocessing and model into a pipeline that cannot leak, and choose and tune models with cross-validation while keeping the test set for one final check. The lessons use `data/customer_churn.csv`; generate it with `python data/make_customer_churn.py` if it is missing.

**Prerequisites:** Parts 1 to 4, and Modules 20 to 23.

## Lessons

1. [24-01 Preprocessing real data](24-01-preprocessing-real-data/lesson.md)
2. [24-02 Pipelines](24-02-pipelines/lesson.md)
3. [24-03 Cross-validation and hyperparameter tuning](24-03-cross-validation-and-tuning/lesson.md)

## Checkpoint quiz

1. Why one-hot encode `payment_method` rather than numbering its categories 0 to 3? When is numbering appropriate?
2. What does `handle_unknown="ignore"` do, and why does a deployed model need it?
3. Feature selection on the whole dataset gave 89% cross-validated accuracy on pure noise. What went wrong, and how does a pipeline fix it?
4. What does 5-fold cross-validation do, and why is it better than a single validation split?
5. After a grid search, when may you look at the test set, and how many times?

<details>
<summary>Answers</summary>

1. Numbering invents an order and distances that do not exist. Numbering (ordinal encoding) is right when the categories really are ordered, like low < medium < high.
2. It encodes a category not seen in training as all zeros instead of raising an error, so new data with an unexpected value does not crash the model.
3. The selection saw the validation labels, so it picked features that matched them by chance: leakage. Inside a pipeline, selection is refitted on each training fold only, giving the honest 52%.
4. It splits the training data into 5 folds, trains on 4 and validates on 1, five times, and averages. Every row is used for validation once, so the estimate is much less noisy, and the spread shows how much it varies.
5. Only after the model is chosen and tuned, once, to report its final performance. Changing the model because of the test score would make it optimistic.

</details>

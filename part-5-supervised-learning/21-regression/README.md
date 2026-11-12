# Module 21: Regression

Predict numbers. You will fit and interpret linear regression with scikit-learn, evaluate it with the right metric and residual plots, let it fit curves with polynomial features while controlling overfitting with Ridge and Lasso, and scale features so that distance-based and regularised models work properly.

**Prerequisites:** Parts 1 to 4, and Module 20.

## Lessons

1. [21-01 Linear regression](21-01-linear-regression/lesson.md)
2. [21-02 Regression metrics](21-02-regression-metrics/lesson.md)
3. [21-03 Polynomial features and regularisation](21-03-polynomial-features-and-regularisation/lesson.md)
4. [21-04 Feature scaling](21-04-feature-scaling/lesson.md)

## Checkpoint quiz

1. A house-price model has a coefficient of 1,500 for floor area in m². What does it mean, and what must you be careful about?
2. A model has R² = −0.3 on the test set. What does that mean?
3. When would you prefer RMSE to MAE?
4. What is the difference between Ridge and Lasso, and what does a larger alpha do?
5. Why must a scaler be fitted on the training data only, and which models do not need scaling?

<details>
<summary>Answers</summary>

1. Each extra m² adds 1,500 to the predicted price, with the other features held constant. It describes association, not cause, and is unreliable if area is strongly correlated with other features (such as number of rooms).
2. The model is worse than simply predicting the mean of the target for everyone, a sign of severe overfitting or a broken model.
3. When large errors are disproportionately costly, because squaring makes RMSE punish them more.
4. Ridge shrinks all coefficients (penalising their squares); Lasso can set some exactly to zero (penalising absolute values), selecting features. Larger alpha means stronger regularisation and a simpler model.
5. Fitting on all the data leaks information from the test set. Tree-based models (decision trees, random forests, gradient boosting) do not need scaling.

</details>

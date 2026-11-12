# Module 22: Classification

Predict categories. You will use logistic regression and read its probabilities, measure classifiers properly with the confusion matrix, precision and recall, tune the decision threshold with ROC and precision-recall curves, and add three more classifiers to your toolkit: k-nearest neighbours, Naive Bayes and support vector machines.

**Prerequisites:** Parts 1 to 4, and Modules 20 and 21.

## Lessons

1. [22-01 Logistic regression](22-01-logistic-regression/lesson.md)
2. [22-02 Classification metrics](22-02-classification-metrics/lesson.md)
3. [22-03 Thresholds, ROC and precision-recall curves](22-03-thresholds-roc-and-precision-recall/lesson.md)
4. [22-04 k-nearest neighbours](22-04-k-nearest-neighbours/lesson.md)
5. [22-05 Naive Bayes](22-05-naive-bayes/lesson.md)
6. [22-06 Support vector machines](22-06-support-vector-machines/lesson.md)

## Checkpoint quiz

1. What does the sigmoid function do in logistic regression, and where is the decision boundary?
2. A spam filter has precision 0.99 and recall 0.60. Describe its behaviour in plain words.
3. Why might you lower the decision threshold below 0.5?
4. Which of k-NN, Naive Bayes and SVMs need scaled features, and why?
5. What do `C` (in logistic regression and SVMs) and `gamma` (in an RBF SVM) control?

<details>
<summary>Answers</summary>

1. It turns the linear score into a probability between 0 and 1. The boundary is where the probability is 0.5, which is where the linear score is 0.
2. When it marks an email as spam it is almost always right (few false alarms), but it lets 40% of spam through (many misses).
3. When missing a positive is much more costly than a false alarm, such as in cancer screening: a lower threshold raises recall.
4. k-NN and SVMs, because they rely on distances, which are dominated by features with large ranges. Naive Bayes models each feature separately, so scaling makes no difference.
5. `C` controls regularisation: smaller C means a simpler model (a wider margin for SVMs). `gamma` controls how far each training point's influence reaches: large gamma gives very local, wiggly boundaries that overfit.

</details>

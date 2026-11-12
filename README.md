# Python to Machine Learning: Course Curriculum

A self-paced course that goes from writing your first line of Python to building supervised and unsupervised machine learning models with scikit-learn.

This README is the **master outline**. The lesson content itself is built out module by module from this document. If you are the model (or person) building the course, read [Build Instructions](#build-instructions) first.

- **Audience:** complete beginners to programming. No maths beyond high-school algebra assumed.
- **Outcome:** the learner can load a dataset, explore it, choose and train an appropriate model, evaluate it honestly, and explain what the model is doing.
- **Size:** 7 parts, 27 modules, 113 lessons, 6 part projects and 1 capstone.
- **Estimated effort:** 120 to 150 hours.

## Contents

- [Course Map](#course-map)
- [Build Instructions](#build-instructions)
- [Part 1: Python Fundamentals](#part-1-python-fundamentals)
- [Part 2: Intermediate Python](#part-2-intermediate-python)
- [Part 3: The Data Toolkit](#part-3-the-data-toolkit)
- [Part 4: Maths for Machine Learning](#part-4-maths-for-machine-learning)
- [Part 5: Supervised Learning](#part-5-supervised-learning)
- [Part 6: Unsupervised Learning](#part-6-unsupervised-learning)
- [Part 7: Capstone](#part-7-capstone)
- [Build Progress](#build-progress)

## Course Map

| Part | Theme | Modules | Lessons | Ends with |
|------|-------|---------|---------|-----------|
| 1 | Python Fundamentals | 01 to 07 | 30 | Project: text-based expense tracker |
| 2 | Intermediate Python | 08 to 12 | 20 | Project: log file analyser package |
| 3 | The Data Toolkit | 13 to 16 | 17 | Project: exploratory data analysis report |
| 4 | Maths for Machine Learning | 17 to 19 | 12 | Project: linear regression from scratch |
| 5 | Supervised Learning | 20 to 24 | 21 | Project: end-to-end classification pipeline |
| 6 | Unsupervised Learning | 25 to 27 | 13 | Project: customer segmentation |
| 7 | Capstone | n/a | n/a | Capstone: full ML project of the learner's choice |

Parts must be taken in order. Each module assumes everything before it and nothing after it.

## Build Instructions

These rules are for whoever generates the lesson content. Follow them exactly so that every module looks and behaves the same.

### How to work

1. Build **one module per session**. Do not start a module until the previous one passes its checks.
2. Before writing, read this section and the outline for the module you are building. Also skim the outline of the module before it, so you know what the learner already knows.
3. Create every lesson in the module, then the module `README.md`, then run the checks in [Definition of done](#definition-of-done).
4. Tick the module in [Build Progress](#build-progress).

### Environment

- Python 3.11 or newer. Use only syntax that works on 3.11.
- Dependencies go in a single `requirements.txt` at the repo root: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `pytest`. Add nothing else without a reason stated in the module README.
- Parts 1 and 2 use the **standard library only** (plus `pytest` for the tests).
- Module 01 tells the learner how to create a virtual environment and install `requirements.txt`.

### Repository layout

```
py-training/
├── README.md                     # this file
├── requirements.txt
├── data/                         # small CSV files created by the builder (see Datasets)
├── part-1-python-fundamentals/
│   ├── 01-getting-started/
│   │   ├── README.md             # module overview: goals, lesson list, checkpoint quiz
│   │   ├── 01-01-running-python/
│   │   │   ├── lesson.md
│   │   │   ├── examples.py
│   │   │   ├── ex_01_01.py
│   │   │   ├── sol_01_01.py
│   │   │   └── test_ex_01_01.py
│   │   └── 01-02-.../
│   └── project/                  # the part project
│       ├── README.md             # brief, requirements, stretch goals
│       ├── starter/
│       └── solution/
├── part-2-intermediate-python/
└── ...
```

- Lesson IDs are `MM-LL` (module number, lesson number), exactly as listed in this outline.
- Lesson folder name is the ID plus a short kebab-case title, for example `05-03-dictionaries`.
- Exercise, solution and test files carry the lesson ID in the file name (`ex_05_03.py`). File names must be unique across the whole repo, otherwise pytest cannot collect them.

### Files in every lesson

| File | Contents |
|------|----------|
| `lesson.md` | The teaching text. Structure below. |
| `examples.py` | Every code example from `lesson.md`, runnable top to bottom with `python examples.py`. Must exit without error. |
| `ex_MM_LL.py` | 3 to 6 exercises as function stubs. Each stub has a docstring that states the task, with one example input and output, and a body of `raise NotImplementedError`. |
| `sol_MM_LL.py` | The same functions, fully implemented, with a short comment where the approach is not obvious. |
| `test_ex_MM_LL.py` | pytest tests, at least 2 per exercise, including one edge case. |

Test files must load the module under test like this, so the same tests check both the learner's work and the reference solutions:

```python
import importlib
import os

mod = importlib.import_module(
    "sol_05_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_05_03"
)
```

Lessons marked **(concept)** in the outline have no exercise, solution or test files. They have `lesson.md` and `examples.py` only, and `lesson.md` ends with 5 written review questions and their answers.

### Structure of `lesson.md`

Use these headings, in this order:

1. `# MM-LL Title`
2. `## What you will learn`: 2 to 4 bullet points, each starting with a verb.
3. `## Why it matters`: 2 to 3 sentences linking the topic to something the learner will build.
4. `## Concepts`: the teaching. Short explanation, then a code example, then what the output is and why. Repeat per concept. Keep each code block under 25 lines.
5. `## Common mistakes`: 2 to 4 real errors beginners make, each with the error message or wrong output and the fix.
6. `## Try it`: one small experiment to run in the REPL or by editing `examples.py`.
7. `## Exercises`: one line per exercise, pointing at `ex_MM_LL.py`, and the command to run the tests.
8. `## Summary`: 3 to 5 bullet points.

### Writing rules

- Target 600 to 1,200 words per lesson. One main idea per lesson.
- Use only Python features and libraries taught in the current lesson or earlier ones. If you need something later in the outline, you are in the wrong lesson.
- Define every technical term the first time it appears.
- Show real output for every example. Run the code, do not guess the output.
- Variable names are full words (`total_price`, not `tp`).
- From Part 3 onward, set `random_state=42` (or `np.random.default_rng(42)`) everywhere randomness is involved, so the learner sees the same numbers as the lesson.
- Plots: `examples.py` saves figures to a `figures/` folder inside the lesson with `plt.savefig`, and `lesson.md` embeds them. Never call `plt.show()` in files that the tests run.
- Part 5 and 6 lessons that introduce an algorithm follow this order: the intuition in plain words, a tiny worked example by hand or in NumPy, the scikit-learn version, the main hyperparameters, when it works well, when it fails.
- No maths notation without a sentence that says the same thing in words.

### Datasets

Lessons must run offline. Use only:

- Datasets bundled with scikit-learn: `load_iris`, `load_wine`, `load_breast_cancer`, `load_diabetes`, `load_digits`.
- Generators: `make_classification`, `make_regression`, `make_blobs`, `make_moons`, `make_circles`.
- Small CSV files (under 1,000 rows) that the builder writes into `data/` with a generator script stored next to them (`data/make_<name>.py`, fixed seed). The outline says where these are needed.

Do not use datasets that download on first use (`fetch_*` in scikit-learn, `seaborn.load_dataset`).

### Module README

Each module folder has a `README.md` with: a 2 to 3 sentence overview, prerequisites (module numbers), the lesson list with links, and a 5-question checkpoint quiz with answers in a collapsed `<details>` block.

### Part projects

Each part ends with a project in `part-N-.../project/`. The project `README.md` contains the brief, numbered requirements, a suggested order of work, and 2 to 3 stretch goals. `starter/` holds a skeleton with tests for the numbered requirements. `solution/` holds a complete reference solution that passes those tests. A project uses only material from its own part and earlier parts.

### Definition of done

A module is done when all of these pass, run from the repo root:

```bash
# 1. every examples.py in the module runs cleanly
for f in part-*/MM-*/*/examples.py; do python "$f" || echo "FAILED: $f"; done

# 2. the reference solutions pass every test in the module
COURSE_SOLUTIONS=1 pytest part-*/MM-*

# 3. the unsolved exercises are collected and fail (they must not error at import)
pytest part-*/MM-* --co -q
```

Replace `MM` with the module number. Also check that every lesson listed in this outline for the module exists, and that no lesson uses a feature taught later.

---

## Part 1: Python Fundamentals

Goal: the learner can write small, correct programs using variables, control flow, functions and the built-in collections. Standard library only.

### Module 01: Getting Started

- **01-01 Installing and running Python** (concept): installing Python, the REPL, running a `.py` file, choosing an editor, reading the terminal.
- **01-02 Your first program**: `print`, comments, statements, how Python runs code top to bottom, reading a traceback.
- **01-03 Virtual environments and pip** (concept): what a package is, `python -m venv`, activating, `pip install -r requirements.txt`, running `pytest` for this course.

### Module 02: Values, Variables and Types

- **02-01 Numbers and arithmetic**: `int`, `float`, operators, `//`, `%`, `**`, operator precedence, float rounding surprises.
- **02-02 Variables and assignment**: names, assignment, reassignment, naming rules and conventions, augmented assignment.
- **02-03 Strings**: quotes, escaping, concatenation, indexing, slicing, `len`, immutability.
- **02-04 String methods and f-strings**: `lower`, `strip`, `replace`, `split`, `join`, `find`, `in`, f-string formatting of numbers.
- **02-05 Booleans, None and type conversion**: `bool`, comparison operators, `None`, `int()`, `float()`, `str()`, truthiness, `type()`, `input()`.

### Module 03: Control Flow

- **03-01 Conditionals**: `if`, `elif`, `else`, nesting, conditional expressions.
- **03-02 Boolean logic**: `and`, `or`, `not`, short-circuiting, chained comparisons.
- **03-03 while loops**: loop conditions, counters, `break`, `continue`, avoiding infinite loops.
- **03-04 for loops and range**: iterating over strings and `range`, accumulator pattern, nested loops.
- **03-05 Loop patterns**: counting, summing, searching, min and max by hand, `else` on loops, `enumerate`.

### Module 04: Functions

- **04-01 Defining and calling functions**: `def`, parameters, arguments, `return` versus `print`, docstrings.
- **04-02 Arguments in depth**: positional and keyword arguments, default values, the mutable default trap.
- **04-03 Scope**: local and global names, why globals cause bugs, passing data in and out.
- **04-04 Functions as building blocks**: decomposing a problem, pure functions, functions calling functions, type hints as documentation.
- **04-05 Reading and writing tests**: `assert`, how the course tests work, writing a first pytest test.

### Module 05: Collections

- **05-01 Lists**: creating, indexing, slicing, mutating, `append`, `extend`, `insert`, `pop`, `remove`, `sort` versus `sorted`.
- **05-02 Tuples and unpacking**: immutability, packing and unpacking, swapping, returning multiple values, `zip`.
- **05-03 Dictionaries**: key-value pairs, lookup, `get`, adding and deleting, iterating `keys`, `values`, `items`, counting pattern.
- **05-04 Sets**: uniqueness, membership tests, union, intersection, difference.
- **05-05 Nested data and references**: lists of dicts, dicts of lists, aliasing, shallow versus deep copy.
- **05-06 Comprehensions**: list, dict and set comprehensions, filtering, when a plain loop is clearer.

### Module 06: Files and Errors

- **06-01 Reading and writing text files**: `open`, `with`, reading lines, writing, file modes, `pathlib.Path`.
- **06-02 CSV and JSON**: the `csv` module, `DictReader`, `json.load` and `json.dump`, mapping file data to lists and dicts.
- **06-03 Exceptions**: reading tracebacks, `try`, `except`, `else`, `finally`, catching specific exceptions.
- **06-04 Raising errors and validating input**: `raise`, choosing an exception type, fail-early checks, custom exception classes (brief).

### Module 07: Problem Solving and Debugging

- **07-01 Breaking down a problem** (concept): restating the problem, examples first, pseudocode, solving a simpler version.
- **07-02 Debugging**: print debugging, `breakpoint()` and basic `pdb` commands, reading a stack trace, bisecting a bug.

### Part 1 Project: Expense Tracker

A command-line program that records expenses (date, category, amount, note) in a JSON file and supports add, list, filter by category, monthly totals and a per-category summary. Validates input and handles a missing or corrupt data file.

---

## Part 2: Intermediate Python

Goal: the learner can organise code into modules and classes, use the standard library fluently, and write code that other people can read and test. Standard library only.

### Module 08: Modules and Project Structure

- **08-01 Imports and modules**: `import`, `from ... import`, aliases, `if __name__ == "__main__"`, how Python finds modules.
- **08-02 Packages**: folders as packages, `__init__.py`, relative versus absolute imports, laying out a small project.
- **08-03 Standard library tour**: `math`, `random`, `datetime`, `collections` (`Counter`, `defaultdict`), `itertools` basics.
- **08-04 Command-line programs**: `sys.argv`, `argparse`, exit codes.

### Module 09: Object-Oriented Programming

- **09-01 Classes and instances**: `class`, `__init__`, attributes, methods, `self`.
- **09-02 Special methods**: `__repr__`, `__str__`, `__eq__`, `__len__`, making objects sortable.
- **09-03 Inheritance and composition**: subclasses, `super()`, overriding, when to prefer composition.
- **09-04 Dataclasses and properties**: `@dataclass`, default fields, `@property`, class versus instance attributes.
- **09-05 The estimator pattern**: designing a class with `fit` and `predict` methods. Builds a tiny `MeanPredictor` class as a preview of the scikit-learn interface used in Part 5.

### Module 10: Functional Tools and Iteration

- **10-01 Functions as values**: passing functions, `lambda`, `sorted` with `key`, `map` and `filter` versus comprehensions.
- **10-02 Iterators and generators**: the iteration protocol, `yield`, generator expressions, laziness and memory.
- **10-03 `*args`, `**kwargs` and unpacking**: variadic functions, argument unpacking in calls, keyword-only arguments.
- **10-04 Decorators and closures**: closures, writing a simple decorator, `functools.wraps`, a timing decorator.

### Module 11: Writing Reliable Code

- **11-01 Testing with pytest**: test structure, `pytest.raises`, parametrised tests, fixtures (basic).
- **11-02 Type hints**: annotating functions and collections, `Optional`, why hints help, not enforced at runtime.
- **11-03 Style and readability**: PEP 8 essentials, naming, function length, docstrings, refactoring a messy script.
- **11-04 Context managers and logging**: `with` beyond files, `contextlib.contextmanager`, the `logging` module versus `print`.

### Module 12: Performance and Complexity

- **12-01 Measuring code**: `time.perf_counter`, `timeit`, measuring before optimising.
- **12-02 Big-O intuition**: constant, linear, quadratic and logarithmic growth, list versus set versus dict lookup cost.
- **12-03 Why loops are slow for numbers**: summing a million numbers in pure Python, motivating vectorised libraries. Bridge to Part 3.

### Part 2 Project: Log File Analyser

An installable package with a command-line entry point that parses a web server log (generated sample file provided in `data/`), and reports requests per status code, the busiest hours, the top paths and the slowest requests. Uses classes for parsed records, generators for reading large files, and has a pytest test suite.

---

## Part 3: The Data Toolkit

Goal: the learner can load, clean, reshape, summarise and visualise tabular data with NumPy, pandas, Matplotlib and seaborn.

### Module 13: NumPy

- **13-01 Arrays**: `ndarray` versus list, creating arrays, `dtype`, `shape`, `ndim`, `arange`, `linspace`, `zeros`, `ones`.
- **13-02 Indexing and slicing**: 1-D and 2-D indexing, slices as views, boolean masks, fancy indexing.
- **13-03 Vectorised operations and broadcasting**: element-wise arithmetic, universal functions, broadcasting rules with pictures, replacing a loop.
- **13-04 Aggregations and axes**: `sum`, `mean`, `std`, `min`, `max`, `argmax`, the `axis` argument, `reshape`.
- **13-05 Random numbers and linear algebra basics**: `default_rng`, sampling, seeds, `@` and `dot`, transpose. Preview of Module 17.

### Module 14: pandas

Needs `data/store_sales.csv` (about 500 rows: date, store, product category, units, unit price, with some missing values and a few duplicates) and `data/stores.csv` (store, city, region).

- **14-01 Series and DataFrames**: creating, `read_csv`, `head`, `info`, `describe`, columns and index, dtypes.
- **14-02 Selecting and filtering**: column selection, `loc` versus `iloc`, boolean filters, `isin`, `query`, sorting.
- **14-03 Cleaning data**: missing values (`isna`, `dropna`, `fillna`), duplicates, fixing types, string methods via `.str`, renaming.
- **14-04 Creating and transforming columns**: vectorised column maths, `apply`, `map`, `astype`, binning with `cut`, dates with `to_datetime` and `.dt`.
- **14-05 Grouping and aggregating**: `groupby`, `agg` with several functions, `value_counts`, `pivot_table`.
- **14-06 Combining tables**: `merge` and join types, `concat`, checking a merge for lost or duplicated rows.

### Module 15: Visualisation

- **15-01 Matplotlib fundamentals**: figure and axes, line and scatter plots, labels, titles, legends, saving figures.
- **15-02 Chart types and when to use them**: bar, histogram, box plot, scatter. Matching a chart to a question.
- **15-03 Subplots and styling**: `plt.subplots` grids, shared axes, colours, annotations, readable defaults.
- **15-04 Statistical plots with seaborn**: `histplot`, `boxplot`, `scatterplot` with `hue`, `pairplot`, `heatmap` of a correlation matrix (using DataFrames built from scikit-learn datasets).

### Module 16: Exploratory Data Analysis

- **16-01 An EDA workflow**: shape, types, missing values, distributions, relationships, written findings. A repeatable checklist.
- **16-02 Outliers, skew and correlation**: spotting outliers, log transforms, correlation versus causation, Simpson's paradox example.

### Part 3 Project: EDA Report

A full exploratory analysis of the wine dataset (`load_wine` converted to a DataFrame) plus the store sales CSV: cleaning steps, at least six well-chosen figures, and a written `REPORT.md` with five findings, each backed by a number or chart.

---

## Part 4: Maths for Machine Learning

Goal: the learner has working intuition for the maths that models rely on, expressed in NumPy code rather than proofs. Every idea is shown as code and a picture.

### Module 17: Linear Algebra

- **17-01 Vectors**: vectors as points and arrows, addition, scaling, length (norm), distance between points.
- **17-02 Dot product and similarity**: dot product, angle, cosine similarity, projection.
- **17-03 Matrices**: a dataset as a matrix (rows are samples, columns are features), matrix-vector and matrix-matrix multiplication, transpose, shapes that fit.
- **17-04 Linear models as matrix maths**: predictions as `X @ w + b`, identity and inverse (intuition), solving a small system with `np.linalg.solve`.

### Module 18: Calculus and Optimisation

- **18-01 Functions, slopes and derivatives**: slope of a line, derivative as slope at a point, numerical derivative with a small step.
- **18-02 Gradients**: functions of several inputs, partial derivatives, the gradient as the direction of steepest increase.
- **18-03 Loss functions**: what "error" means, mean squared error, plotting loss against a parameter.
- **18-04 Gradient descent**: the update rule, learning rate too small and too large, convergence, implementing it in NumPy for a one-variable problem then two.

### Module 19: Probability and Statistics

- **19-01 Describing data**: mean, median, mode, variance, standard deviation, percentiles, z-scores.
- **19-02 Probability basics**: events, conditional probability, independence, Bayes' rule with a medical test example.
- **19-03 Distributions and sampling**: uniform, normal and binomial distributions, simulating with NumPy, the central limit theorem by simulation.
- **19-04 Covariance, correlation and sampling error**: covariance, Pearson correlation, sample versus population, why results vary between samples (bootstrap demonstration).

### Part 4 Project: Linear Regression From Scratch

Implement a `LinearRegressionGD` class in NumPy with `fit`, `predict` and a stored loss history. Train it on `make_regression` data and on `load_diabetes`, plot the loss curve, and compare the learned weights with `np.linalg.lstsq`.

---

## Part 5: Supervised Learning

Goal: the learner can frame a prediction problem, train and tune regression and classification models with scikit-learn, and evaluate them without fooling themselves.

### Module 20: Machine Learning Foundations

- **20-01 What machine learning is** (concept): learning from examples versus writing rules, features and targets, supervised versus unsupervised versus reinforcement learning, regression versus classification.
- **20-02 The scikit-learn interface**: estimators, `fit`, `predict`, `score`, `X` and `y` shapes, a first model in ten lines.
- **20-03 Train and test splits**: why we hold data out, `train_test_split`, stratification, data leakage.
- **20-04 Overfitting and underfitting**: model complexity, the bias-variance trade-off shown with polynomial fits, learning curves.
- **20-05 Baselines**: `DummyClassifier` and `DummyRegressor`, why every model needs a baseline to beat.

### Module 21: Regression

- **21-01 Linear regression**: fitting a line and a plane, coefficients and intercept, interpreting weights, residuals.
- **21-02 Regression metrics**: MAE, MSE, RMSE, R squared, choosing a metric, residual plots.
- **21-03 Polynomial features and regularisation**: `PolynomialFeatures`, Ridge and Lasso, the effect of `alpha`, Lasso as feature selection.
- **21-04 Feature scaling**: why scale matters, `StandardScaler`, `MinMaxScaler`, fit on train only.

### Module 22: Classification

- **22-01 Logistic regression**: from a linear score to a probability with the sigmoid, decision boundary, `predict_proba`, multi-class.
- **22-02 Classification metrics**: confusion matrix, accuracy and why it misleads, precision, recall, F1, class imbalance.
- **22-03 Thresholds, ROC and precision-recall curves**: changing the threshold, ROC curve and AUC, precision-recall curve, picking a threshold for a cost.
- **22-04 k-nearest neighbours**: distance-based prediction, choosing `k`, why scaling is essential, the curse of dimensionality (intuition).
- **22-05 Naive Bayes**: Bayes' rule applied to classification, the independence assumption, `GaussianNB`, where it is strong and weak.
- **22-06 Support vector machines**: margins, support vectors, `C`, the kernel trick with `make_moons`, `gamma`.

### Module 23: Tree-Based Models

- **23-01 Decision trees**: splits, Gini impurity and entropy, reading a plotted tree, depth and overfitting, pruning parameters.
- **23-02 Random forests**: bagging, random feature subsets, out-of-bag score, feature importances and their limits.
- **23-03 Gradient boosting**: boosting as correcting earlier errors, `GradientBoostingClassifier` and `HistGradientBoostingClassifier`, learning rate versus number of trees, early stopping.

### Module 24: The Modelling Workflow

- **24-01 Preprocessing real data**: encoding categories (`OneHotEncoder`, `OrdinalEncoder`), imputing missing values, `ColumnTransformer`. Uses a generated `data/customer_churn.csv` with mixed numeric and categorical columns and missing values.
- **24-02 Pipelines**: `Pipeline` and `make_pipeline`, why pipelines prevent leakage, saving a model with `joblib`.
- **24-03 Cross-validation and hyperparameter tuning**: k-fold, `cross_val_score`, `GridSearchCV`, `RandomizedSearchCV`, keeping a final test set untouched.

### Part 5 Project: End-to-End Classification

Predict customer churn from `data/customer_churn.csv`. Deliver an EDA summary, a baseline, a preprocessing-plus-model pipeline, a comparison of at least three model families using cross-validation, a tuned final model, test-set metrics with a confusion matrix and ROC curve, and a short write-up of which features matter and what the model gets wrong.

---

## Part 6: Unsupervised Learning

Goal: the learner can find structure in unlabelled data with clustering and dimensionality reduction, and judge whether that structure is real.

### Module 25: Clustering

- **25-01 What unsupervised learning is** (concept): no labels, the kinds of questions it answers, why evaluation is harder, typical uses.
- **25-02 k-means**: centroids, the assign-and-update loop implemented in NumPy, then `KMeans`, initialisation and `n_init`, scaling.
- **25-03 Choosing the number of clusters**: inertia and the elbow method, silhouette score, silhouette plots, when no answer is clear.
- **25-04 Hierarchical clustering**: agglomerative clustering, linkage types, reading a dendrogram, cutting the tree.
- **25-05 DBSCAN**: density-based clusters, `eps` and `min_samples`, noise points, shapes k-means cannot find (`make_moons`).
- **25-06 Gaussian mixture models**: soft cluster membership, `GaussianMixture`, covariance types, choosing components with BIC.

### Module 26: Dimensionality Reduction

- **26-01 Why reduce dimensions**: visualisation, noise, speed, the curse of dimensionality revisited.
- **26-02 Principal component analysis**: directions of greatest variance, PCA step by step in NumPy on 2-D data, then `PCA`, components and loadings.
- **26-03 Using PCA well**: explained variance ratio, choosing the number of components, scaling first, PCA inside a pipeline, reconstructing `load_digits` images.
- **26-04 t-SNE for visualisation**: neighbour-preserving embeddings, perplexity, what distances in the plot do and do not mean, t-SNE versus PCA on digits.

### Module 27: Applied Unsupervised Learning

- **27-01 Anomaly detection**: outliers as a learning problem, `IsolationForest`, `LocalOutlierFactor`, contamination, checking flagged points.
- **27-02 Interpreting and validating clusters**: profiling clusters with group statistics, stability across seeds, comparing with known labels when available (adjusted Rand index).
- **27-03 Unsupervised steps in supervised pipelines**: PCA as preprocessing, cluster labels as features, measuring whether they help.

### Part 6 Project: Customer Segmentation

Segment customers in a generated `data/customers.csv` (spend, visit frequency, recency, basket size, channel). Scale and reduce the data, compare k-means, hierarchical clustering and a Gaussian mixture, justify the number of segments, visualise them in two dimensions, and write a plain-language profile of each segment.

---

## Part 7: Capstone

The learner picks one of three briefs, or proposes their own, and completes it without step-by-step guidance. The builder writes `part-7-capstone/README.md` containing the briefs, a project checklist and a marking rubric, plus one complete reference solution for brief A.

- **Brief A, prediction:** predict disease progression (`load_diabetes`) or tumour diagnosis (`load_breast_cancer`). Full supervised workflow with a justified choice of metric.
- **Brief B, discovery:** explore `load_digits` without using the labels. Reduce, cluster and characterise the groups, then use the labels only at the end to check what the clusters found.
- **Brief C, combined:** on the churn data, segment customers with clustering, then test whether segment membership improves a churn classifier.

Every capstone must include:

1. A problem statement and a success measure, written before any modelling.
2. EDA with written findings.
3. A baseline and at least two candidate approaches.
4. Honest evaluation on held-out data (supervised) or a stability and interpretability check (unsupervised).
5. A `REPORT.md` covering method, results, limitations and what to try next.
6. Code organised into importable modules with tests for the data-preparation functions.

---

## Build Progress

Tick a module when it meets the [Definition of done](#definition-of-done).

**Setup**
- [x] `requirements.txt` and `.gitignore` (add `.venv/`, `__pycache__/`, `.pytest_cache/`, `figures/` is **not** ignored)

**Part 1: Python Fundamentals**
- [x] 01 Getting Started
- [x] 02 Values, Variables and Types
- [x] 03 Control Flow
- [x] 04 Functions
- [x] 05 Collections
- [x] 06 Files and Errors
- [x] 07 Problem Solving and Debugging
- [x] Project: Expense Tracker

**Part 2: Intermediate Python**
- [x] 08 Modules and Project Structure
- [x] 09 Object-Oriented Programming
- [x] 10 Functional Tools and Iteration
- [x] 11 Writing Reliable Code
- [x] 12 Performance and Complexity
- [x] Project: Log File Analyser

**Part 3: The Data Toolkit**
- [x] 13 NumPy
- [x] 14 pandas
- [x] 15 Visualisation
- [x] 16 Exploratory Data Analysis
- [x] Project: EDA Report

**Part 4: Maths for Machine Learning**
- [x] 17 Linear Algebra
- [x] 18 Calculus and Optimisation
- [x] 19 Probability and Statistics
- [x] Project: Linear Regression From Scratch

**Part 5: Supervised Learning**
- [x] 20 Machine Learning Foundations
- [x] 21 Regression
- [x] 22 Classification
- [x] 23 Tree-Based Models
- [x] 24 The Modelling Workflow
- [ ] Project: End-to-End Classification

**Part 6: Unsupervised Learning**
- [ ] 25 Clustering
- [ ] 26 Dimensionality Reduction
- [ ] 27 Applied Unsupervised Learning
- [ ] Project: Customer Segmentation

**Part 7: Capstone**
- [ ] Capstone briefs, rubric and reference solution

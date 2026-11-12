# 24-01 Preprocessing real data

## What you will learn

- Split real data into features and target, and into training and test sets, before any preprocessing.
- Encode categories with `OneHotEncoder` and `OrdinalEncoder`.
- Fill missing values with `SimpleImputer`.
- Apply a different recipe to each group of columns with `ColumnTransformer`.

## Why it matters

The datasets in Modules 20 to 23 were clean grids of numbers. Real data has text categories, gaps and columns on wildly different scales, and scikit-learn models accept only complete numeric arrays. Preprocessing turns one into the other. Done carelessly it leaks information from the test set or breaks on new data; done with the tools in this lesson it is short, repeatable and safe.

## Concepts

### The churn data

`data/customer_churn.csv` describes 2,000 customers of a subscription service and whether each one left (**churned**). Generate it with `python data/make_customer_churn.py` if it is missing.

```python
churn = pd.read_csv(DATA / "customer_churn.csv")
print(churn.shape)
print(churn.dtypes.value_counts().to_string())
print(churn.isna().sum()[churn.isna().sum() > 0].to_string())
print(churn["churned"].mean().round(3))
```

```
(2000, 11)
str        6
int64      3
float64    2
monthly_charges     52
total_charges       48
payment_method      79
satisfaction       115
0.277
```

Six text columns, five numeric, gaps in four columns, and 27.7% of customers churned. The columns fall into groups that each need different treatment:

| Group | Columns | Treatment |
|--|--|--|
| identifier | `customer_id` | drop: it identifies, it does not predict |
| numeric | `tenure_months`, `monthly_charges`, `total_charges`, `support_calls` | fill gaps, scale |
| nominal (unordered categories) | `contract`, `payment_method`, `internet_service`, `region` | fill gaps, one-hot encode |
| ordinal (ordered categories) | `satisfaction` (low < medium < high) | fill gaps, encode as 0, 1, 2 |
| target | `churned` | keep separate |

### Split first

Every preprocessing step **learns** something: the median used to fill gaps, the mean and spread used to scale, the list of categories. These must be learned from the training data only, or information from the test set leaks into the model (20-03). So split first:

```python
X = churn.drop(columns=["customer_id", "churned"])
y = churn["churned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(X_train.shape, X_test.shape)
```

```
(1600, 9) (400, 9)
```

### One-hot encoding

A model cannot multiply "two-year" by a weight. Numbering the categories 0, 1, 2 would invent an order and distances that do not exist (is "card" really halfway between "bank transfer" and "electronic check"?). **One-hot encoding** instead creates one 0/1 column per category:

```python
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(X_train[["contract"]])
print(encoder.get_feature_names_out())
print(X_train["contract"].head(3).tolist())
print(encoded[:3])
```

```
['contract_month-to-month' 'contract_one-year' 'contract_two-year']
['month-to-month', 'two-year', 'two-year']
[[1. 0. 0.]
 [0. 0. 1.]
 [0. 0. 1.]]
```

Each row has a single 1 in the column for its category. Encoders take a 2-D input, hence the double brackets `[["contract"]]`. `sparse_output=False` returns an ordinary array; by default the encoder returns a **sparse** matrix, which stores only the non-zero values to save memory (fine to pass to models, harder to print). `pd.get_dummies` (14-04) does something similar, but an encoder **remembers** the categories it saw in training, so the test set gets exactly the same columns.

### Categories never seen in training

What if a new customer has a category the encoder never saw?

```python
strict = OneHotEncoder(sparse_output=False).fit(pd.DataFrame({"contract": ["one-year", "two-year"]}))
try:
    strict.transform(pd.DataFrame({"contract": ["month-to-month"]}))
except ValueError as error:
    print("ValueError:", str(error).splitlines()[0])
tolerant = OneHotEncoder(sparse_output=False, handle_unknown="ignore").fit(pd.DataFrame({"contract": ["one-year", "two-year"]}))
print(tolerant.transform(pd.DataFrame({"contract": ["month-to-month"]})))
```

```
ValueError: Found unknown categories ['month-to-month'] in column 0 during transform
[[0. 0.]]
```

By default, it raises an error. **`handle_unknown="ignore"`** encodes an unknown category as all zeros instead, so a deployed model keeps working. Use it for real models.

### Ordinal encoding

When categories **do** have a natural order, encode them as numbers in that order with **`OrdinalEncoder`**, giving the order explicitly (otherwise it sorts alphabetically: high, low, medium):

```python
ordinal = OrdinalEncoder(categories=[["low", "medium", "high"]])
print(ordinal.fit_transform(pd.DataFrame({"satisfaction": ["high", "low", "medium"]})).ravel())
```

```
[2. 0. 1.]
```

One column instead of three, and a model can learn "higher satisfaction, less churn" with a single weight.

### Imputing missing values

Most models refuse `NaN`. **Imputation** fills each gap with an estimate. `SimpleImputer` learns one value per column from the training data:

```python
imputer = SimpleImputer(strategy="median")
filled = imputer.fit_transform(X_train[["monthly_charges", "total_charges"]])
print(imputer.statistics_.round(2))
print(np.isnan(filled).sum())
most_frequent = SimpleImputer(strategy="most_frequent").fit(X_train[["payment_method"]])
print(most_frequent.statistics_)
```

```
[  64.83 1385.55]
0
['card']
```

- `"median"` for numbers: robust to outliers and skew (19-01).
- `"mean"` for roughly symmetric numbers.
- `"most_frequent"` for categories.
- `"constant"` with `fill_value="missing"` treats "missing" as a category of its own, which helps when the gap itself carries information.

Adding `add_indicator=True` also appends a 0/1 column saying "this value was missing", so the model can learn from missingness itself.

### ColumnTransformer: one recipe per group

**`ColumnTransformer`** applies a different transformer to each group of columns and joins the results side by side. Each entry is `(name, transformer, columns)`. When a group needs two steps in a row (impute, then scale), they are chained with a `Pipeline`, which 24-02 covers fully; for now, read it as "do these steps in order":

```python
numeric = ["tenure_months", "monthly_charges", "total_charges", "support_calls"]
nominal = ["contract", "payment_method", "internet_service", "region"]
ordered = ["satisfaction"]

numeric_steps = [("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]

preprocess = ColumnTransformer([
    ("numeric", Pipeline(numeric_steps), numeric),
    ("nominal", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("encode", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), nominal),
    ("ordered", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("encode", OrdinalEncoder(categories=[["low", "medium", "high"]]))]), ordered),
])
train_ready = preprocess.fit_transform(X_train)
test_ready = preprocess.transform(X_test)
print(train_ready.shape, test_ready.shape)
print(list(preprocess.get_feature_names_out())[:6])
print(np.isnan(train_ready).sum(), np.isnan(test_ready).sum())
```

```
(1600, 19) (400, 19)
['numeric__tenure_months', 'numeric__monthly_charges', 'numeric__total_charges', 'numeric__support_calls', 'nominal__contract_month-to-month', 'nominal__contract_one-year']
0 0
```

Nine messy columns became 19 clean numeric ones: 4 numeric, 14 one-hot (3 + 4 + 3 + 4 categories) and 1 ordinal, with no gaps. The crucial pattern: **`fit_transform` on the training set, `transform` on the test set**. The test set is filled with the training medians and encoded with the training categories. `get_feature_names_out` tells you what each output column means, which you need when reading coefficients or importances. Columns not listed in any group are dropped (set `remainder="passthrough"` to keep them unchanged).

## Common mistakes

- **Preprocessing before splitting.** Imputing or scaling the whole dataset lets test statistics leak into training.
- **Calling `fit_transform` on the test set.** It re-learns medians and categories from the test data. Use `transform`.
- **Encoding nominal categories as integers.** It invents an order. Use one-hot encoding unless the categories really are ordered.
- **Keeping identifier columns.** An ID is unique to each row; a model can memorise it and learn nothing useful.
- **Forgetting `handle_unknown="ignore"`.** The model crashes on the first unfamiliar category in production.

## Try it

Change the ordinal group to be one-hot encoded instead, and the numeric imputer to `SimpleImputer(strategy="median", add_indicator=True)`. How many output columns are there now? Use `get_feature_names_out` to check what the new ones are.

## Exercises

Open `ex_24_01.py`:

1. `missing_report`: the count of missing values per column, only columns with gaps, largest first.
2. `split_churn`: drop the ID, separate the target, and make a stratified train/test split.
3. `column_groups`: sort columns into numeric and text.
4. `build_preprocessor`: the `ColumnTransformer` from this lesson.

Run the tests:

```
python -m pytest part-5-supervised-learning/24-modelling-workflow/24-01-preprocessing-real-data
```

## Summary

- Split into training and test sets before any preprocessing, then fit every transformer on the training data only.
- `OneHotEncoder(handle_unknown="ignore")` turns unordered categories into 0/1 columns and survives unseen categories.
- `OrdinalEncoder(categories=[[...]])` encodes ordered categories in the order you give.
- `SimpleImputer` fills gaps with the median, mean, most frequent value or a constant learned from training data.
- `ColumnTransformer` applies a different recipe to each column group; `get_feature_names_out` names the output columns.

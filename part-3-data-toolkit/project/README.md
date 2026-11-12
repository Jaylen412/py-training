# Part 3 Project: EDA Report

## Brief

Explore two datasets and write a short report of what you find, as you would before building any model:

- **Wine** (`sklearn.datasets.load_wine`): 178 wines from three cultivars, 13 chemical measurements each. Which measurements tell the cultivars apart?
- **Store sales** (`data/store_sales.csv` and `data/stores.csv`): three months of messy daily sales data for six stores. Clean it, then find out what drives revenue.

Your report, `REPORT.md`, must contain your cleaning steps, at least six well-chosen figures, and five findings, each backed by a number or a chart.

This project uses everything from Part 3: NumPy (13), pandas cleaning, features, grouping and merging (14), Matplotlib and seaborn (15), and the EDA checklist with its warnings about outliers, skew and correlation (16).

## Getting started

Work in `starter/`. `eda.py` has a function for each requirement, with a docstring saying what it must do, and a `main()` that prints the numbers you need and saves your figures. `REPORT.md` is a template to fill in.

```
python -m pytest part-3-data-toolkit/project/starter
python part-3-data-toolkit/project/starter/eda.py
```

Until `clean_sales` and `add_features` work, the tests that depend on them show as ERROR (their shared set-up fails) rather than FAILED.

## Requirements

1. `load_wine_frame`, `wine_summary` and `strongest_wine_correlations` load and summarise the wine data.
2. `clean_sales` produces 468 clean rows: no duplicates, tidy categories, real dates, no missing values, with missing prices filled **per category**.
3. `add_features` adds revenue, month, weekday and weekend columns.
4. `sales_summary` returns the headline numbers listed in its docstring.
5. `make_figures` saves at least six titled, labelled figures covering both datasets.
6. `REPORT.md` has a **Findings** section with at least five numbered findings, each containing a number, and embeds at least six figures that exist.

## Suggested order of work

1. Do a quick EDA of each dataset in the REPL or a scratch script, following the 16-01 checklist, before writing any project code.
2. Requirements 1 to 4, running the tests after each function.
3. Requirement 5: sketch each figure in a scratch script first, then move it into `make_figures`. For each one, write down the question it answers.
4. Run `eda.py`, then write `REPORT.md` from its output and your figures. Put the most important finding first.
5. Reread your findings with 16-02 in mind: is any of them really caused by a confounder? Say so under limitations.

## Stretch goals

1. Add a figure and a finding about the breast cancer dataset from 16-01, comparing it with the wine data: which one looks easier to classify, and why?
2. Find the store-and-category combination whose revenue grew or fell most between January and March, and plot all of them as small multiples.
3. Write tests for two of your figure functions that check their titles and axis labels (as in Module 15's tests).

## Reference solution

`solution/` contains a complete `eda.py`, its figures and a finished `REPORT.md`. Write your own before reading it. To run the tests against it:

```
COURSE_SOLUTIONS=1 python -m pytest part-3-data-toolkit/project/starter
```

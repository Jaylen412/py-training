# Module 14: pandas

Work with real tables. You will load CSV files into DataFrames, select and filter rows and columns, clean missing values, duplicates and messy text, engineer new columns, summarise by group, and combine tables with merges you can trust.

**Prerequisites:** Parts 1 and 2, and Module 13.

**Data:** `data/store_sales.csv` (486 rows of daily sales, deliberately messy) and `data/stores.csv` (store details). Recreate them with `python data/make_store_sales.py`.

## Lessons

1. [14-01 Series and DataFrames](14-01-series-and-dataframes/lesson.md)
2. [14-02 Selecting and filtering](14-02-selecting-and-filtering/lesson.md)
3. [14-03 Cleaning data](14-03-cleaning-data/lesson.md)
4. [14-04 Creating and transforming columns](14-04-creating-and-transforming-columns/lesson.md)
5. [14-05 Grouping and aggregating](14-05-grouping-and-aggregating/lesson.md)
6. [14-06 Combining tables](14-06-combining-tables/lesson.md)

## Checkpoint quiz

1. What is the difference between `df.loc[0:2]` and `df.iloc[0:2]`?
2. Why did the `units` column load as `float64` even though it counts whole items?
3. Name two ways to deal with missing values, and one risk of each.
4. Write a line that gives the mean `units` for each `category`.
5. You left-merge 460 sales rows with a store table and get 541 rows. What happened, and how do you prevent it?

<details>
<summary>Answers</summary>

1. `loc` selects by label and includes the end, giving rows labelled 0, 1 and 2; `iloc` selects by position and excludes the end, giving the first two rows.
2. Some values were missing, and pandas stores missing numbers as `NaN`, which is a float, so the whole column became float.
3. Dropping rows (loses data, and can bias what is left if missingness is not random); filling with a value such as the median (invents values that may be wrong, shrinking the apparent spread).
4. `sales.groupby("category")["units"].mean()`.
5. A key appears more than once in the store table, so matching sales rows were duplicated. Check row counts after merging and pass `validate="many_to_one"`.

</details>

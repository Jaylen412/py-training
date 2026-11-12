"""Solutions for 16-01 An EDA workflow."""
import pandas as pd


def overview(frame):
    """Return rows, columns, missing values and duplicate rows."""
    rows, columns = frame.shape
    return {
        "rows": rows,
        "columns": columns,
        "missing": int(frame.isna().sum().sum()),
        "duplicates": int(frame.duplicated().sum()),
    }


def missing_report(frame):
    """Return counts and percentages of missing values per affected column."""
    counts = frame.isna().sum()
    counts = counts[counts > 0].sort_values(ascending=False)
    return pd.DataFrame({"count": counts, "percent": (counts / len(frame) * 100).round(1)})


def class_balance(labels):
    """Return the proportion of each class."""
    proportions = labels.value_counts(normalize=True)
    return {label: round(float(share), 3) for label, share in proportions.items()}


def median_by_group(frame, group_column, columns):
    """Return the median of `columns` for each group."""
    return frame.groupby(group_column)[columns].median()


def numbered_findings(findings):
    """Number the findings, one per line."""
    return "\n".join(f"{number}. {finding}" for number, finding in enumerate(findings, start=1))

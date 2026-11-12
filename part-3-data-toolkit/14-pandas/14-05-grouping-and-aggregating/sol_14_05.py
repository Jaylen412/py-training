"""Solutions for 14-05 Grouping and aggregating."""
import pandas as pd


def rows_per_category(sales):
    """Return {category: number of rows}."""
    return {category: int(count) for category, count in sales["category"].value_counts().items()}


def revenue_by_store(sales):
    """Return total revenue per store, largest first."""
    return sales.groupby("store")["revenue"].sum().sort_values(ascending=False)


def category_summary(sales):
    """Return named summaries per category."""
    return sales.groupby("category").agg(
        rows=("units", "size"),
        total_units=("units", "sum"),
        average_price=("unit_price", "mean"),
        revenue=("revenue", "sum"),
    )


def store_category_table(sales):
    """Return a store-by-category grid of total revenue."""
    return sales.pivot_table(
        index="store", columns="category", values="revenue", aggfunc="sum", fill_value=0
    )


def fill_price_by_category(sales):
    """Fill missing prices with the median price of their category."""
    filled = sales.copy()
    category_medians = filled.groupby("category")["unit_price"].transform("median")
    filled["unit_price"] = filled["unit_price"].fillna(category_medians)
    return filled

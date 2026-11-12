"""Solutions for 14-04 Creating and transforming columns."""
import pandas as pd


def add_revenue(sales):
    """Add a revenue column."""
    return sales.assign(revenue=sales["units"] * sales["unit_price"])


def add_city(sales, cities):
    """Add a city column from a store lookup."""
    return sales.assign(city=sales["store"].map(lambda store: cities.get(store, "Unknown")))


def add_size_band(sales):
    """Bin units into small, medium and large."""
    size = pd.cut(sales["units"], bins=[-1, 5, 20, 100], labels=["small", "medium", "large"])
    return sales.assign(size=size)


def add_date_parts(sales):
    """Convert dates and add month, weekday and is_weekend columns."""
    dates = pd.to_datetime(sales["date"])
    return sales.assign(
        date=dates,
        month=dates.dt.month,
        weekday=dates.dt.day_name(),
        is_weekend=dates.dt.day_of_week >= 5,
    )

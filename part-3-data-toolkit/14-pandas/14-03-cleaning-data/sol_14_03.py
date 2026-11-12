"""Solutions for 14-03 Cleaning data."""
import pandas as pd


def clean_categories(categories):
    """Strip and title-case category names."""
    return categories.str.strip().str.title()


def drop_missing(frame, columns):
    """Return rows with no missing value in `columns`."""
    return frame.dropna(subset=columns)


def fill_with_median(frame, column):
    """Fill missing values in `column` with its median."""
    filled = frame.copy()
    filled[column] = filled[column].fillna(filled[column].median())
    return filled


def remove_duplicates(frame):
    """Remove duplicate rows and renumber the index."""
    return frame.drop_duplicates().reset_index(drop=True)


def clean_sales(raw):
    """Apply the full cleaning pipeline."""
    cleaned = remove_duplicates(raw)
    cleaned["category"] = clean_categories(cleaned["category"])
    cleaned["date"] = pd.to_datetime(cleaned["date"])
    cleaned = drop_missing(cleaned, ["units"])
    cleaned = fill_with_median(cleaned, "unit_price")
    return cleaned.reset_index(drop=True)

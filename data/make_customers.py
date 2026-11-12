"""Generate data/customers.csv for Part 6.

Run from the repository root:
    python data/make_customers.py

customers.csv has 1,200 rows, one per shopper, with the columns
    customer_id, annual_spend, visits_per_month, days_since_last_visit,
    avg_basket_size, channel
`channel` is "store", "online" or "both". There are no labels: the file is
built from four hidden groups of shoppers (the group is NOT saved), so a
good clustering should find about four segments.
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
FOLDER = Path(__file__).parent

# name: (share, spend, visits, recency, basket, channel probabilities store/online/both)
SEGMENTS = {
    "loyal regulars":   (0.30, (2400, 350), (9.0, 1.8), (6, 4),   (38, 8),  (0.55, 0.15, 0.30)),
    "big-basket":       (0.20, (3600, 500), (2.5, 0.8), (22, 8),  (95, 15), (0.60, 0.10, 0.30)),
    "bargain hunters":  (0.25, (700, 150),  (5.0, 1.2), (14, 6),  (14, 4),  (0.30, 0.50, 0.20)),
    "lapsed":           (0.25, (450, 120),  (0.8, 0.4), (110, 35), (30, 9), (0.40, 0.35, 0.25)),
}


def main():
    rng = np.random.default_rng(SEED)
    rows = []
    for share, spend, visits, recency, basket, channel_p in SEGMENTS.values():
        n = int(round(1200 * share))
        rows.append(pd.DataFrame({
            "annual_spend": rng.normal(*spend, n).clip(50),
            "visits_per_month": rng.normal(*visits, n).clip(0.1),
            "days_since_last_visit": rng.normal(*recency, n).clip(1),
            "avg_basket_size": rng.normal(*basket, n).clip(3),
            "channel": rng.choice(["store", "online", "both"], size=n, p=channel_p),
        }))
    frame = pd.concat(rows, ignore_index=True).sample(frac=1, random_state=SEED).reset_index(drop=True)
    frame["annual_spend"] = frame["annual_spend"].round(2)
    frame["visits_per_month"] = frame["visits_per_month"].round(1)
    frame["days_since_last_visit"] = frame["days_since_last_visit"].round().astype(int)
    frame["avg_basket_size"] = frame["avg_basket_size"].round(2)
    frame.insert(0, "customer_id", [f"U{number:05d}" for number in range(1, len(frame) + 1)])

    path = FOLDER / "customers.csv"
    frame.to_csv(path, index=False)
    print(f"wrote {path} with {len(frame)} rows")
    print(frame.describe().round(1).to_string())


if __name__ == "__main__":
    main()

"""Generate data/customer_churn.csv for Module 24 and the Part 5 project.

Run from the repository root:
    python data/make_customer_churn.py

customer_churn.csv has 2,000 rows, one per customer of a subscription
service, with the columns:
    customer_id, tenure_months, monthly_charges, total_charges,
    support_calls, contract, payment_method, internet_service,
    region, satisfaction, churned
`churned` is 1 if the customer left (about a quarter of them).
Numeric and categorical columns both have some missing values, and
`satisfaction` is an ordered category (low < medium < high).
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
FOLDER = Path(__file__).parent
N = 2000


def main():
    rng = np.random.default_rng(SEED)
    contract = rng.choice(["month-to-month", "one-year", "two-year"], size=N, p=[0.55, 0.25, 0.20])
    payment = rng.choice(["card", "bank transfer", "electronic check", "mailed check"], size=N, p=[0.3, 0.25, 0.3, 0.15])
    internet = rng.choice(["fibre", "dsl", "none"], size=N, p=[0.45, 0.4, 0.15])
    region = rng.choice(["North", "South", "East", "West"], size=N)

    longer = np.where(contract == "two-year", 30, np.where(contract == "one-year", 18, 0))
    tenure = np.clip(rng.exponential(18, N) + longer, 1, 72).round().astype(int)
    base = np.select([internet == "fibre", internet == "dsl"], [80.0, 55.0], 25.0)
    monthly = np.round(base + rng.normal(0, 12, N), 2).clip(18, 120)
    total = np.round(monthly * tenure * rng.uniform(0.95, 1.05, N), 2)
    support_calls = rng.poisson(1.2 + 1.5 * (internet == "fibre") * rng.random(N), N)
    satisfaction_score = rng.normal(0, 1, N) - 0.35 * support_calls
    satisfaction = np.select([satisfaction_score < -1.0, satisfaction_score < 0.4], ["low", "medium"], "high")

    # The churn score: higher means more likely to leave.
    score = (
        -2.0
        + 1.3 * (contract == "month-to-month")
        - 0.8 * (contract == "two-year")
        - 0.045 * tenure
        + 0.018 * (monthly - 60)
        + 0.30 * support_calls
        + 0.6 * (payment == "electronic check")
        + 0.4 * (internet == "fibre")
        + 0.9 * (satisfaction == "low")
        - 0.6 * (satisfaction == "high")
        + rng.normal(0, 0.6, N)
    )
    churned = (rng.random(N) < 1 / (1 + np.exp(-score))).astype(int)

    frame = pd.DataFrame({
        "customer_id": [f"C{number:05d}" for number in range(1, N + 1)],
        "tenure_months": tenure,
        "monthly_charges": monthly,
        "total_charges": total,
        "support_calls": support_calls,
        "contract": contract,
        "payment_method": payment,
        "internet_service": internet,
        "region": region,
        "satisfaction": satisfaction,
        "churned": churned,
    })

    # Knock out some values so that imputation is needed.
    for column, share in [("total_charges", 0.03), ("monthly_charges", 0.02),
                          ("payment_method", 0.04), ("satisfaction", 0.05)]:
        frame.loc[rng.random(N) < share, column] = np.nan

    path = FOLDER / "customer_churn.csv"
    frame.to_csv(path, index=False)
    print(f"wrote {path} with {len(frame)} rows, churn rate {frame['churned'].mean():.3f}")
    print(frame.isna().sum()[frame.isna().sum() > 0].to_string())


if __name__ == "__main__":
    main()

import pandas as pd

# Load dataset
perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv",
    sep="\t"
)

print("Original Shape:", perf.shape)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio numeric
perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

# Flag return anomalies
anomalies = perf[
    (perf["return_1yr_pct"] < -100) |
    (perf["return_1yr_pct"] > 500)
]

print("Return anomalies:", len(anomalies))

# Check expense ratio range (0.1% - 2.5%)
expense_anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("Expense ratio anomalies:", len(expense_anomalies))

# Remove duplicates
perf = perf.drop_duplicates()

print("Cleaned Shape:", perf.shape)

# Save cleaned file
perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("scheme_performance cleaned successfully!")
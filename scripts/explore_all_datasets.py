import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

for file in sorted(raw_path.glob("*.csv")):
    print("=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    try:
        # Read tab-separated files
        df = pd.read_csv(file, sep="\t")
    except Exception:
        # Fallback for comma-separated files
        df = pd.read_csv(file)

    print("\nShape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")
from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(exist_ok=True)
DATASETS = {
    "01_fund_master.csv": "\t",
    "02_nav_history.csv": "\t",
    "03_aum_by_fund_house.csv": "\t",
    "04_monthly_sip_inflows.csv": "\t",
    "05_category_inflows.csv": "\t",
    "06_industry_folio_count.csv": "\t",
    "07_scheme_performance.csv": "\t",
    "08_investor_transactions.csv": "\t",
    "09_portfolio_holdings.csv": "\t",
    "10_benching_indices.csv": "\t"
}
for filename, separator in DATASETS.items():

    print(f"\nProcessing {filename}")

    df = pd.read_csv(RAW_PATH / filename, sep=separator)

    original_rows = len(df)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows where every value is missing
    df = df.dropna(how="all")

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Trim whitespace from text columns
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    # Convert date columns
    for col in df.columns:
        if "date" in col or "month" in col:
            try:
                df[col] = pd.to_datetime(df[col], dayfirst=True)
            except Exception:
                pass

    output_file = PROCESSED_PATH / filename.replace(".csv", "_clean.csv")

    df.to_csv(output_file, index=False)

    print(f"Saved: {output_file.name}")
    print(f"Rows: {original_rows} → {len(df)}")
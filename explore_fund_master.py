import pandas as pd

# Read dataset
df = pd.read_csv(
    "data/raw/01_fund_master.csv",
    sep="\t"
)

print("=" * 60)
print("UNIQUE FUND HOUSES")
print(df["fund_house"].unique())

print("\n" + "=" * 60)
print("UNIQUE CATEGORIES")
print(df["category"].unique())

print("\n" + "=" * 60)
print("UNIQUE SUB CATEGORIES")
print(df["sub_category"].unique())

print("\n" + "=" * 60)
print("UNIQUE RISK CATEGORIES")
print(df["risk_category"].unique())

print("\n" + "=" * 60)
print("COUNTS")

print("Fund Houses:", df["fund_house"].nunique())
print("Categories:", df["category"].nunique())
print("Sub Categories:", df["sub_category"].nunique())
print("Risk Categories:", df["risk_category"].nunique())
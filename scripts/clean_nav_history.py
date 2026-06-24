import pandas as pd

# Load dataset
nav = pd.read_csv(
    "data/raw/02_nav_history.csv",
    sep="\t"
)

print("Original Shape:", nav.shape)

# Convert date
nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

# Sort by fund and date
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill missing NAV values
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)

# Keep only valid NAV values
nav = nav[nav["nav"] > 0]

print("Cleaned Shape:", nav.shape)

# Save cleaned file
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("nav_history cleaned successfully!")
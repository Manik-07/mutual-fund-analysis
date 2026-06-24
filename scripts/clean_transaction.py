import pandas as pd

# Read tab-separated file
txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv",
    sep="\t"
)

print("Original Shape:", txn.shape)

# Standardize transaction type
txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

mapping = {
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
}

txn["transaction_type"] = txn["transaction_type"].replace(mapping)

# Fix dates
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    format="%d-%m-%Y",
    errors="coerce"
)

# Amount validation
txn = txn[txn["amount_inr"] > 0]

# KYC validation
valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = txn[
    ~txn["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Records:", len(invalid_kyc))

# Remove duplicates
txn = txn.drop_duplicates()

print("Cleaned Shape:", txn.shape)

# Save
txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("investor_transactions cleaned successfully!")
import pandas as pd
import sqlite3

# Read CSV files
nav_csv = pd.read_csv("data/processed/nav_history_clean.csv")
txn_csv = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf_csv = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Connect DB
conn = sqlite3.connect("bluestock_mf.db")

# Read table counts
nav_db = pd.read_sql("SELECT COUNT(*) AS count FROM nav_history", conn)
txn_db = pd.read_sql("SELECT COUNT(*) AS count FROM investor_transactions", conn)
perf_db = pd.read_sql("SELECT COUNT(*) AS count FROM scheme_performance", conn)

print("NAV CSV Rows:", len(nav_csv))
print("NAV DB Rows :", nav_db.iloc[0, 0])

print("\nTransaction CSV Rows:", len(txn_csv))
print("Transaction DB Rows :", txn_db.iloc[0, 0])

print("\nPerformance CSV Rows:", len(perf_csv))
print("Performance DB Rows :", perf_db.iloc[0, 0])

conn.close()
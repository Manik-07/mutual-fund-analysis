import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")
print(df.columns)
print(df.head())
print(df.info())
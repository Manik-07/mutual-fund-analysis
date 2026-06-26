import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")
print(df.columns)
print(df.head())
print(df.info())
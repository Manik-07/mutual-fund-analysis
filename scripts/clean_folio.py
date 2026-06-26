import pandas as pd

df = pd.read_csv("data/raw/06_industry_folio_count.csv")
print(df.columns)
print(df.head())
print(df.info())
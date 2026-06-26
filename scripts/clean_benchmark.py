import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")
print(df.columns)
print(df.head())
print(df.info())
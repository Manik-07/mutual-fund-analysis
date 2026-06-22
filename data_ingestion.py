import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        print("\n" + "="*70)
        print(file)

        df = pd.read_csv(
            os.path.join(folder, file),
            sep="\t"
        )

        print("Shape:", df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
        
        
      
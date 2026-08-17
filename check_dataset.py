import pandas as pd

data = pd.read_csv("dataset/urls.csv")

print("Columns:")
print(data.columns.tolist())

print("\nNumber of rows:", len(data))

print("\nFirst 5 rows:")
print(data.head())
import pandas as pd

data = pd.read_csv("dataset/features.csv")

print("Columns:")
print(data.columns.tolist())

print("\nShape:")
print(data.shape)

print("\nFirst 5 rows:")
print(data.head())
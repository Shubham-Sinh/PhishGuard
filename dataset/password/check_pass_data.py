import pandas as pd

DATASET_PATH = "dataset/password/pwlds_main.csv"

df = pd.read_csv(DATASET_PATH)

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== COLUMNS =====")
print(df.columns.tolist())

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== FIRST 10 ROWS =====")
print(df.head(10))

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATES =====")
print(df.duplicated().sum())

print("\n===== LABEL DISTRIBUTION =====")
print(df.iloc[:, -1].value_counts().sort_index())
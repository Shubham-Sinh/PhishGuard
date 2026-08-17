import pandas as pd

data = pd.read_csv("dataset/clean_urls.csv")

print("Total URLs:", len(data))

print("\nLabel distribution:")
print(data["label"].value_counts())

print("\nLegitimate URLs:")
print(data[data["label"] == 0]["url"].head(20).to_string(index=False))

print("\nPhishing URLs:")
print(data[data["label"] == 1]["url"].head(20).to_string(index=False))

print("\nExact google.com:")
print(
    data[
        data["url"].str.strip().str.lower() == "google.com"
    ].to_string(index=False)
)
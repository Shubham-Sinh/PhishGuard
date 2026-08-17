import pandas as pd

# Read original dataset
data = pd.read_csv("dataset/urls.csv")

# Store all phishing URLs
phishing_columns = [
    "PHISING URL ",
    "Unnamed: 1",
    "Unnamed: 2",
    "Unnamed: 3",
    "Unnamed: 4",
    "Unnamed: 5",
    "Unnamed: 6"
]

phishing_urls = data[phishing_columns].stack().dropna()

# Store all safe URLs
safe_urls = data["SAFE URL"].dropna()

# Create separate dataframes
phishing_data = pd.DataFrame({
    "url": phishing_urls.values,
    "label": 1
})

safe_data = pd.DataFrame({
    "url": safe_urls.values,
    "label": 0
})

# Combine them
clean_data = pd.concat(
    [phishing_data, safe_data],
    ignore_index=True
)

# Remove duplicates
clean_data = clean_data.drop_duplicates()

# Remove empty URLs
clean_data = clean_data[clean_data["url"].str.strip() != ""]

# Save clean dataset
clean_data.to_csv("dataset/clean_urls.csv", index=False)

print("Dataset prepared successfully!")
print("Total URLs:", len(clean_data))
print("\nLabel distribution:")
print(clean_data["label"].value_counts())
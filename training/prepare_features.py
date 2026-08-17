import pandas as pd

from features.extractor import extract_features


# Load cleaned dataset
data = pd.read_csv("dataset/clean_urls.csv")

print("Total URLs:", len(data))
print("Extracting features...")


# Extract features
X = data["url"].apply(extract_features)


# Names of the 19 features
feature_names = [
    "url_length",
    "dot_count",
    "hyphen_count",
    "has_at",
    "uses_https",
    "digit_count",
    "special_char_count",
    "keyword_count",
    "has_ip",
    "is_shortened",
    "domain_length",
    "domain_dot_count",
    "subdomain_count",
    "path_length",
    "query_length",
    "query_parameter_count",
    "suspicious_tld",
    "domain_letter_count",
    "digit_ratio",
    "vowel_count",
    "consonant_count",
    "unique_char_count",
    "domain_entropy"
]


# Convert features to DataFrame
X = pd.DataFrame(
    X.tolist(),
    columns=feature_names
)


# Add labels
X["label"] = data["label"].values


# Save features
X.to_csv(
    "dataset/features.csv",
    index=False
)


print("Feature extraction completed!")
print("Feature dataset shape:", X.shape)
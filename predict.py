from urllib.parse import urlparse
from config.trusted_domains import load_trusted_domains
import joblib
import pandas as pd

from features.extractor import extract_features


# Feature names used during training
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


# Load trained model
model = joblib.load("models/phishing_model.pkl")

print("Model loaded successfully!")

# Get URL
url = input("\nEnter a URL: ")

# Extract domain
parsed_url = urlparse(
    url if "://" in url else "http://" + url
)

domain = parsed_url.netloc.lower().split("@")[-1].split(":")[0]



# Extract features
features = extract_features(url)

# Convert features into a DataFrame
features_df = pd.DataFrame(
    [features],
    columns=feature_names
)

print("Features:")
print(features_df)

# Make prediction
prediction = model.predict(features_df)[0]

print("\nPrediction:", prediction)

if prediction == 0:
    print("🟢 Legitimate URL")
else:
    print("🔴 Potentially Phishing URL")
import pandas as pd
import joblib

from features.urls_utils import normalize_url


# Load model
model = joblib.load("models/url_character_model.pkl")
vectorizer = joblib.load("models/url_vectorizer.pkl")

# Load test URLs
data = pd.read_csv("test_urls.csv")

# Normalize URLs
urls = data["url"].astype(str).apply(normalize_url)

# Convert to TF-IDF
features = vectorizer.transform(urls)

# Predict
predictions = model.predict(features)

# Results
data["prediction"] = predictions

print("\nEvaluation Results:\n")
print(data.to_string(index=False))

# Accuracy
accuracy = (data["label"] == data["prediction"]).mean() * 100

print(f"\nTest Accuracy: {accuracy:.2f}%")

# Wrong predictions
wrong = data[data["label"] != data["prediction"]]

print("\nIncorrect Predictions:")
print(wrong.to_string(index=False))
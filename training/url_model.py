import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from features.urls_utils import normalize_url

# Load dataset
data = pd.read_csv("dataset/clean_urls.csv")

urls = data["url"].astype(str).apply(normalize_url)
labels = data["label"]

print("Dataset loaded!")
print("Total URLs:", len(urls))


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    urls,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

print("\nGoogle in training set:",
      "google.com" in X_train.str.strip().str.lower().values)

print("Google in testing set:",
      "google.com" in X_test.str.strip().str.lower().values)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# Convert URLs into character n-gram features
vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(3, 5),
    min_df=2,
    max_features=100000
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

print("Vectorization completed!")
print("Training matrix:", X_train_vectorized.shape)


# Train model
model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train_vectorized, y_train)

print("Model training completed!")


# Predictions
predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy * 100, "%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)


# Save model and vectorizer
joblib.dump(
    model,
    "models/url_character_model.pkl"
)

joblib.dump(
    vectorizer,
    "models/url_vectorizer.pkl"
)

print("\nModel and vectorizer saved successfully!")
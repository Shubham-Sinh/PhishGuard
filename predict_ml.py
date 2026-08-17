import joblib


# Load character-based model
model = joblib.load("models/url_character_model.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("models/url_vectorizer.pkl")

print("Character-based ML model loaded successfully!")

# Get URL
url = input("\nEnter a URL: ")

# Convert URL into TF-IDF features
url_features = vectorizer.transform([url])

# Predict
prediction = model.predict(url_features)[0]

print("\nPrediction:", prediction)

if prediction == 0:
    print("🟢 LEGITIMATE URL")
else:
    print("🔴 POTENTIALLY PHISHING URL")
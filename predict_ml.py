import joblib
from features.urls_utils import normalize_url

# Load character-based model
model = joblib.load("models/url_character_model.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("models/url_vectorizer.pkl")

print("Character-based ML model loaded successfully!")

url = input("\nEnter a URL: ")

# Normalize URL exactly like the training data
normalized_url = normalize_url(url)

print("Normalized URL:", normalized_url)

# Convert normalized URL into TF-IDF features
url_features = vectorizer.transform([normalized_url])

# Predict
prediction = model.predict(url_features)[0]
probalities = model.predict_proba(url_features)[0]

legitimate_probability = probalities[0]* 100
phishing_probability = probalities[1] *100

if phishing_probability < 20:
    risk_level = "LOW"
    risk_icon = "🟢"
elif phishing_probability < 50:
    risk_level = "MEDIUM"
    risk_icon = "🟡"
elif phishing_probability < 75:
    risk_level = "HIGH"
    risk_icon = "🟠"
else:
    risk_level = "CRITICAL"
    risk_icon = "🔴"

print("\nPrediction:", prediction)

print(f"Legitimate probability: {legitimate_probability:.2f}%")
print(f"Phishing probability: {phishing_probability:.2f}%")

print(f"Risk Level: {risk_icon} {risk_level}")

if prediction == 0:
    print("\n🟢 LEGITIMATE URL")
else:
    print("\n🔴 POTENTIALLY PHISHING URL")
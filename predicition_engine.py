import re
import joblib

from features.urls_utils import normalize_url


MODEL_PATH = "models/url_character_model.pkl"
VECTORIZER_PATH = "models/url_vectorizer.pkl"


model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def analyze_url_signals(url):
    """
    Extract human-readable security signals from a URL.
    These signals explain characteristics of the URL.
    """

    normalized_url = normalize_url(url)
    lower_url = normalized_url.lower()

    signals = []

    # HTTPS
    if url.lower().startswith("https://"):
        signals.append({
            "type": "safe",
            "title": "HTTPS connection",
            "description": "The URL uses HTTPS encryption."
        })
    else:
        signals.append({
            "type": "warning",
            "title": "No HTTPS",
            "description": "The URL does not use HTTPS."
        })

    # IP address
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}"

    if re.match(ip_pattern, normalized_url):
        signals.append({
            "type": "danger",
            "title": "IP address detected",
            "description": "The URL uses an IP address instead of a domain name."
        })

    # Suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "account",
        "secure",
        "update",
        "password",
        "signin"
    ]

    found_keywords = [
        word for word in suspicious_words
        if word in lower_url
    ]

    if found_keywords:
        signals.append({
            "type": "warning",
            "title": "Suspicious keywords",
            "description": (
                "Detected: " +
                ", ".join(found_keywords)
            )
        })

    # URL shortener
    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "ow.ly",
        "is.gd",
        "buff.ly"
    ]

    if any(shortener in lower_url for shortener in shorteners):
        signals.append({
            "type": "warning",
            "title": "URL shortener detected",
            "description": "Shortened URLs can hide the final destination."
        })

    # @ symbol
    if "@" in url:
        signals.append({
            "type": "danger",
            "title": "@ symbol detected",
            "description": "The URL contains an @ symbol, which can obscure the destination."
        })

    # Hyphen count
    hyphen_count = url.count("-")

    if hyphen_count >= 2:
        signals.append({
            "type": "warning",
            "title": "Multiple hyphens",
            "description": f"The URL contains {hyphen_count} hyphens."
        })

    # URL length
    if len(url) > 100:
        signals.append({
            "type": "warning",
            "title": "Long URL",
            "description": f"The URL contains {len(url)} characters."
        })

    # Digits
    digit_count = sum(char.isdigit() for char in url)

    if digit_count >= 5:
        signals.append({
            "type": "warning",
            "title": "Many digits",
            "description": f"The URL contains {digit_count} digits."
        })

    return signals


def predict_url(url):

    normalized_url = normalize_url(url)

    features = vectorizer.transform([normalized_url])

    prediction = int(model.predict(features)[0])

    probabilities = model.predict_proba(features)[0]

    legitimate_probability = float(probabilities[0] * 100)
    phishing_probability = float(probabilities[1] * 100)

    if phishing_probability < 20:
        risk_level = "LOW"
        risk_icon = "🟢"
        risk_class = "low"

    elif phishing_probability < 50:
        risk_level = "MEDIUM"
        risk_icon = "🟡"
        risk_class = "medium"

    elif phishing_probability < 75:
        risk_level = "HIGH"
        risk_icon = "🟠"
        risk_class = "high"

    else:
        risk_level = "CRITICAL"
        risk_icon = "🔴"
        risk_class = "critical"

    signals = analyze_url_signals(url)

    return {
        "url": url,
        "normalized_url": normalized_url,
        "prediction": prediction,
        "legitimate_probability": legitimate_probability,
        "phishing_probability": phishing_probability,
        "risk_level": risk_level,
        "risk_icon": risk_icon,
        "risk_class": risk_class,
        "signals": signals
    }
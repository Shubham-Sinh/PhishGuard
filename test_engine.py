from predicition_engine import predict_url


urls = [
    "https://google.com",
    "http://192.168.1.10/login",
    "https://secure-login.com/verify/account123"
]


for url in urls:

    result = predict_url(url)

    print("\nURL:", result["url"])
    print("Normalized:", result["normalized_url"])
    print("Prediction:", result["prediction"])
    print(
        "Legitimate:",
        f'{result["legitimate_probability"]:.2f}%'
    )
    print(
        "Phishing:",
        f'{result["phishing_probability"]:.2f}%'
    )
    print("Risk:", result["risk_level"])
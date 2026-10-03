from features.password_features import extract_password_features


test_passwords = [
    "123456",
    "password",
    "hello123",
    "Hello@123",
    "X7@kP9!mQ2#Z"
]


for password in test_passwords:

    features = extract_password_features(password)

    print("\nPassword:", password)
    print("Features:", features)
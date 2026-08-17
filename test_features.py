from features.extractor import extract_features

url = "https://google.com"

features = extract_features(url)

print("URL:", url)
print("Features:", features)
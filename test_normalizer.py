from features.urls_utils import normalize_url


test_urls = [
    "google.com",
    "http://google.com",
    "https://google.com",
    "www.google.com",
    "https://www.google.com/",
    "https://google.com/login"
]

for url in test_urls:
    print(f"{url}  ->  {normalize_url(url)}")
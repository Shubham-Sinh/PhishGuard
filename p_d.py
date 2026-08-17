import re
url = input("Enter a website URL: ")

url_length = len(url)
digit_count = sum(char.isdigit() for char in url)
dot_count = url.count('.')
hyphen_count = url.count('-')
has_at = "@" in url
uses_https = url.startswith("https://")

suspicious_keywords = ["login", "secure", "account", "update", "verify", "update", "password", "signin"]

shorteners = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly"
]

is_shortened = any(shortener in url.lower() for shortener in shorteners)
keyword_count = 0


for keyword in suspicious_keywords:
    if keyword in url:
        keyword_count += 1
        
ip_pattern = r"^(https?://)?(\d{1,3}\.){3}\d{1,3}"

special_chars = "!#$%&'()*+,/:;<=>?@[\\]^_`{|}~"
special_char_count = sum(char in special_chars for char in url)

has_ip = bool(re.match(ip_pattern, url))

risk_score = 0

if url_length > 50:
    risk_score += 1

if dot_count > 3:
    risk_score += 1

if hyphen_count > 2:
    risk_score += 1

if has_at:
    risk_score += 2

if not uses_https:
    risk_score += 1

if digit_count > 5:
    risk_score += 1

if keyword_count >= 2:
    risk_score += 2

if has_ip:
    risk_score += 2

if is_shortened:
    risk_score += 1

print("\nYou entered:", url)
print("URL length:", url_length)
print("Number of digits:", digit_count)
print("Number of dots:", dot_count)
print("Number of hyphens:", hyphen_count)
print("Contains '@':", has_at)
print("Uses HTTPS:", uses_https)
print("Uses URL shortener:", is_shortened)
print("Contains IP address:", has_ip)
print("Number of suspicious keywords found:", keyword_count)
print("Number of special characters:", special_char_count)
print("Risk score:", risk_score)

max_score = 13
risk_percentage = (risk_score / max_score) * 100

print("Risk percentage:", round(risk_percentage, 2), "%")

if risk_percentage < 30:
    print("🟢 LOW RISK")
elif risk_percentage < 60:
    print("🟡 MEDIUM RISK")
else:
    print("🔴 HIGH RISK")
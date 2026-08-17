import re
import math
from urllib.parse import urlparse


def extract_features(url):

    url_lower = url.lower()

    # Make sure URL has a scheme for urlparse()
    parsed_url = urlparse(
        url if "://" in url else "http://" + url
    )

    domain = parsed_url.netloc.split("@")[-1].split(":")[0]
    path = parsed_url.path
    query = parsed_url.query

    # -------------------------
    # Existing features
    # -------------------------

    url_length = len(url)
    dot_count = url.count(".")
    hyphen_count = url.count("-")
    has_at = int("@" in url)
    uses_https = int(url_lower.startswith("https://"))

    digit_count = sum(char.isdigit() for char in url)

    special_chars = "!#$%&'()*+,/:;<=>?@[\\]^_`{|}~"
    special_char_count = sum(
        char in special_chars for char in url
    )

    suspicious_words = [
        "login",
        "verify",
        "account",
        "secure",
        "update",
        "password",
        "signin"
    ]

    keyword_count = sum(
        word in url_lower for word in suspicious_words
    )

    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    has_ip = int(bool(re.match(ip_pattern, domain)))

    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "ow.ly",
        "is.gd",
        "buff.ly"
    ]

    is_shortened = int(
        any(shortener in domain for shortener in shorteners)
    )

    # -------------------------
    # New domain features
    # -------------------------

    domain_length = len(domain)

    domain_dot_count = domain.count(".")

    subdomain_count = max(
        0,
        len(domain.split(".")) - 2
    )

    path_length = len(path)

    query_length = len(query)

    query_parameter_count = (
        query.count("&") + 1
        if query
        else 0
    )

    # Suspicious TLDs often seen in phishing datasets
    suspicious_tlds = [
        ".xyz",
        ".top",
        ".tk",
        ".ml",
        ".ga",
        ".cf",
        ".gq"
    ]

    suspicious_tld = int(
        any(domain.endswith(tld) for tld in suspicious_tlds)
    )

    # Number of alphabetic characters in domain
    domain_letter_count = sum(
        char.isalpha() for char in domain
    )

    # Ratio of digits to domain length
    digit_ratio = (
        digit_count / len(domain)
        if len(domain) > 0
        else 0
    )

    # -------------------------
    # Domain character features
    # -------------------------

    letters_only = [
        char for char in domain
        if char.isalpha()
    ]

    vowel_count = sum(
        char in "aeiou"
        for char in domain.lower()
    )

    consonant_count = sum(
        char.isalpha() and char not in "aeiou"
        for char in domain.lower()
    )

    unique_char_count = len(set(domain.lower()))

    # Shannon entropy of the domain
    if domain:
        frequency = {
            char: domain.lower().count(char)
            for char in set(domain.lower())
        }

        entropy = 0

        for count in frequency.values():
            probability = count / len(domain)
            entropy -= probability * math.log2(probability)
    else:
        entropy = 0


    # -------------------------
    # Return all features
    # -------------------------

    return [
        url_length,
        dot_count,
        hyphen_count,
        has_at,
        uses_https,
        digit_count,
        special_char_count,
        keyword_count,
        has_ip,
        is_shortened,
        domain_length,
        domain_dot_count,
        subdomain_count,
        path_length,
        query_length,
        query_parameter_count,
        suspicious_tld,
        domain_letter_count,
        digit_ratio,
        vowel_count,
        consonant_count,
        unique_char_count,
        entropy
    ]
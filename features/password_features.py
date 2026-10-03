import re
import math


def extract_password_features(password):

    password = str(password)

    length = len(password)

    lowercase_count = sum(c.islower() for c in password)
    uppercase_count = sum(c.isupper() for c in password)
    digit_count = sum(c.isdigit() for c in password)
    special_count = sum(
        not c.isalnum() for c in password
    )

    unique_characters = len(set(password))

    has_lowercase = int(lowercase_count > 0)
    has_uppercase = int(uppercase_count > 0)
    has_digits = int(digit_count > 0)
    has_special = int(special_count > 0)

    character_types = (
        has_lowercase
        + has_uppercase
        + has_digits
        + has_special
    )

    digit_ratio = digit_count / length if length else 0
    special_ratio = special_count / length if length else 0
    unique_ratio = (
        unique_characters / length
        if length else 0
    )

    # Character pool size
    pool_size = 0

    if has_lowercase:
        pool_size += 26

    if has_uppercase:
        pool_size += 26

    if has_digits:
        pool_size += 10

    if has_special:
        pool_size += 32

    # Approximate entropy
    entropy = (
        length * math.log2(pool_size)
        if pool_size > 0
        else 0
    )

    # Repeated consecutive characters
    repeated_characters = int(
        bool(re.search(r"(.)\1", password))
    )

    # Sequential patterns
    sequential_pattern = int(
        bool(
            re.search(
                r"(123|234|345|456|567|678|789|"
                r"abc|bcd|cde|def|qwe|wer|ert)",
                password.lower()
            )
        )
    )

    return [
        length,
        lowercase_count,
        uppercase_count,
        digit_count,
        special_count,
        unique_characters,
        character_types,
        digit_ratio,
        special_ratio,
        unique_ratio,
        entropy,
        repeated_characters,
        sequential_pattern
    ]
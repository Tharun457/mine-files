"""Data validation utilities."""

import re


def is_valid_email(email):
    if not isinstance(email, str):
        raise TypeError("Expected a string")
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def is_valid_url(url):
    if not isinstance(url, str):
        raise TypeError("Expected a string")
    pattern = r"^https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})(?:/[^\s]*)?$"
    return bool(re.match(pattern, url))


def is_strong_password(password):
    if not isinstance(password, str):
        raise TypeError("Expected a string")
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def is_valid_ip(ip):
    if not isinstance(ip, str):
        raise TypeError("Expected a string")
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
        if len(part) > 1 and part[0] == "0":
            return False
    return True


def is_valid_phone(phone):
    if not isinstance(phone, str):
        raise TypeError("Expected a string")
    cleaned = re.sub(r"[\s\-().+]", "", phone)
    if not cleaned.isdigit():
        return False
    return 7 <= len(cleaned) <= 15


def validate_range(value, min_val=None, max_val=None):
    if not isinstance(value, (int, float)):
        raise TypeError("Expected a number")
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True

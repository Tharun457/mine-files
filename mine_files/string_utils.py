"""String manipulation utilities."""


def reverse(s):
    if not isinstance(s, str):
        raise TypeError("Expected a string")
    return s[::-1]


def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Expected a string")
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_words(s):
    if not isinstance(s, str):
        raise TypeError("Expected a string")
    return " ".join(word.capitalize() for word in s.split())


def count_vowels(s):
    if not isinstance(s, str):
        raise TypeError("Expected a string")
    return sum(1 for ch in s.lower() if ch in "aeiou")


def truncate(s, max_length, suffix="..."):
    if not isinstance(s, str):
        raise TypeError("Expected a string")
    if max_length < len(suffix):
        raise ValueError("max_length must be at least as long as suffix")
    if len(s) <= max_length:
        return s
    return s[: max_length - len(suffix)] + suffix


def snake_to_camel(s):
    if not isinstance(s, str):
        raise TypeError("Expected a string")
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def camel_to_snake(s):
    if not isinstance(s, str):
        raise TypeError("Expected a string")
    result = []
    for i, ch in enumerate(s):
        if ch.isupper() and i > 0:
            result.append("_")
        result.append(ch.lower())
    return "".join(result)

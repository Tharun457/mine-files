"""Comprehensive tests for the string_utils module."""

import pytest

from mine_files.string_utils import (
    reverse,
    is_palindrome,
    capitalize_words,
    count_vowels,
    truncate,
    snake_to_camel,
    camel_to_snake,
)


# ── reverse ─────────────────────────────────────────────────────────────────


class TestReverse:
    def test_basic(self):
        assert reverse("hello") == "olleh"

    def test_empty(self):
        assert reverse("") == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            reverse(123)


# ── is_palindrome ───────────────────────────────────────────────────────────


class TestIsPalindrome:
    def test_true(self):
        assert is_palindrome("racecar") is True

    def test_false(self):
        assert is_palindrome("hello") is False

    def test_mixed_case_and_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_palindrome(123)


# ── capitalize_words ────────────────────────────────────────────────────────


class TestCapitalizeWords:
    def test_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_already_capitalized(self):
        assert capitalize_words("Hello") == "Hello"

    def test_empty(self):
        assert capitalize_words("") == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            capitalize_words(123)


# ── count_vowels ────────────────────────────────────────────────────────────


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_uppercase(self):
        assert count_vowels("AEIOU") == 5

    def test_type_error(self):
        with pytest.raises(TypeError):
            count_vowels(123)


# ── truncate ────────────────────────────────────────────────────────────────


class TestTruncate:
    def test_no_truncation(self):
        assert truncate("hi", 10) == "hi"

    def test_truncation(self):
        assert truncate("hello world", 8) == "hello..."

    def test_custom_suffix(self):
        assert truncate("hello world", 8, suffix="~") == "hello w~"

    def test_max_length_too_short(self):
        with pytest.raises(ValueError):
            truncate("hello", 2, suffix="...")

    def test_type_error(self):
        with pytest.raises(TypeError):
            truncate(123, 5)


# ── snake_to_camel ──────────────────────────────────────────────────────────


class TestSnakeToCamel:
    def test_basic(self):
        assert snake_to_camel("hello_world") == "helloWorld"

    def test_single_word(self):
        assert snake_to_camel("hello") == "hello"

    def test_type_error(self):
        with pytest.raises(TypeError):
            snake_to_camel(123)


# ── camel_to_snake ──────────────────────────────────────────────────────────


class TestCamelToSnake:
    def test_basic(self):
        assert camel_to_snake("helloWorld") == "hello_world"

    def test_single_word(self):
        assert camel_to_snake("hello") == "hello"

    def test_multiple_caps(self):
        assert camel_to_snake("myHTTPClient") == "my_h_t_t_p_client"

    def test_type_error(self):
        with pytest.raises(TypeError):
            camel_to_snake(123)

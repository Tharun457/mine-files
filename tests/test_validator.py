"""Comprehensive tests for the validator module."""

import pytest

from mine_files.validator import (
    is_valid_email,
    is_valid_url,
    is_strong_password,
    is_valid_ip,
    is_valid_phone,
    validate_range,
)


# ── is_valid_email ──────────────────────────────────────────────────────────


class TestIsValidEmail:
    def test_simple_valid(self):
        assert is_valid_email("user@example.com") is True

    def test_dots_and_plus(self):
        assert is_valid_email("first.last+tag@sub.domain.org") is True

    def test_missing_at(self):
        assert is_valid_email("userexample.com") is False

    def test_missing_domain(self):
        assert is_valid_email("user@") is False

    def test_missing_tld(self):
        assert is_valid_email("user@domain") is False

    def test_empty_string(self):
        assert is_valid_email("") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_email(123)


# ── is_valid_url ────────────────────────────────────────────────────────────


class TestIsValidUrl:
    def test_http(self):
        assert is_valid_url("http://example.com") is True

    def test_https_with_path(self):
        assert is_valid_url("https://example.com/path/to/page") is True

    def test_no_scheme(self):
        assert is_valid_url("example.com") is False

    def test_ftp_scheme(self):
        assert is_valid_url("ftp://example.com") is False

    def test_empty(self):
        assert is_valid_url("") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_url(42)


# ── is_strong_password ──────────────────────────────────────────────────────


class TestIsStrongPassword:
    def test_strong(self):
        assert is_strong_password("Str0ng!Pass") is True

    def test_too_short(self):
        assert is_strong_password("S1!a") is False

    def test_no_uppercase(self):
        assert is_strong_password("weak1!pass") is False

    def test_no_lowercase(self):
        assert is_strong_password("WEAK1!PASS") is False

    def test_no_digit(self):
        assert is_strong_password("NoDigit!Pass") is False

    def test_no_special(self):
        assert is_strong_password("NoSpecial1Pass") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_strong_password(12345)


# ── is_valid_ip ─────────────────────────────────────────────────────────────


class TestIsValidIp:
    def test_valid(self):
        assert is_valid_ip("192.168.1.1") is True

    def test_all_zeros(self):
        assert is_valid_ip("0.0.0.0") is True

    def test_max(self):
        assert is_valid_ip("255.255.255.255") is True

    def test_out_of_range(self):
        assert is_valid_ip("256.0.0.1") is False

    def test_leading_zero(self):
        assert is_valid_ip("192.168.01.1") is False

    def test_too_few_octets(self):
        assert is_valid_ip("192.168.1") is False

    def test_non_numeric(self):
        assert is_valid_ip("abc.def.ghi.jkl") is False

    def test_empty(self):
        assert is_valid_ip("") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_ip(12345)


# ── is_valid_phone ──────────────────────────────────────────────────────────


class TestIsValidPhone:
    def test_simple(self):
        assert is_valid_phone("1234567890") is True

    def test_with_dashes(self):
        assert is_valid_phone("123-456-7890") is True

    def test_international(self):
        assert is_valid_phone("+1 (555) 123-4567") is True

    def test_too_short(self):
        assert is_valid_phone("123") is False

    def test_letters(self):
        assert is_valid_phone("abc-def-ghij") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_phone(12345)


# ── validate_range ──────────────────────────────────────────────────────────


class TestValidateRange:
    def test_in_range(self):
        assert validate_range(5, min_val=0, max_val=10) is True

    def test_below_min(self):
        assert validate_range(-1, min_val=0) is False

    def test_above_max(self):
        assert validate_range(11, max_val=10) is False

    def test_no_bounds(self):
        assert validate_range(999) is True

    def test_float(self):
        assert validate_range(3.14, min_val=0.0, max_val=4.0) is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_range("five")

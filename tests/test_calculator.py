"""Comprehensive tests for the calculator module."""

import pytest

from mine_files.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    factorial,
    gcd,
    lcm,
)


# ── basic arithmetic ────────────────────────────────────────────────────────


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


# ── power ───────────────────────────────────────────────────────────────────


class TestPower:
    def test_positive_exponent(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == pytest.approx(0.5)

    def test_zero_base_negative_exp(self):
        with pytest.raises(ValueError):
            power(0, -1)


# ── factorial ───────────────────────────────────────────────────────────────


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_positive(self):
        assert factorial(5) == 120

    def test_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_non_integer(self):
        with pytest.raises(TypeError):
            factorial(3.5)


# ── gcd / lcm ──────────────────────────────────────────────────────────────


class TestGcdLcm:
    def test_gcd_basic(self):
        assert gcd(12, 8) == 4

    def test_gcd_coprime(self):
        assert gcd(7, 13) == 1

    def test_gcd_with_zero(self):
        assert gcd(0, 5) == 5

    def test_gcd_negative(self):
        assert gcd(-12, 8) == 4

    def test_lcm_basic(self):
        assert lcm(4, 6) == 12

    def test_lcm_with_zero(self):
        assert lcm(0, 5) == 0

    def test_lcm_same(self):
        assert lcm(7, 7) == 7

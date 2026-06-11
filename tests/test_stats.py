"""Comprehensive tests for the stats module."""

import math

import pytest

from mine_files.stats import (
    mean,
    median,
    mode,
    variance,
    std_dev,
    percentile,
    z_score,
    correlation,
)


# ── mean ────────────────────────────────────────────────────────────────────


class TestMean:
    def test_integers(self):
        assert mean([1, 2, 3, 4, 5]) == 3.0

    def test_single(self):
        assert mean([7]) == 7.0

    def test_floats(self):
        assert mean([1.5, 2.5]) == 2.0

    def test_empty(self):
        with pytest.raises(ValueError):
            mean([])


# ── median ──────────────────────────────────────────────────────────────────


class TestMedian:
    def test_odd_count(self):
        assert median([3, 1, 2]) == 2

    def test_even_count(self):
        assert median([1, 2, 3, 4]) == 2.5

    def test_single(self):
        assert median([42]) == 42

    def test_empty(self):
        with pytest.raises(ValueError):
            median([])


# ── mode ────────────────────────────────────────────────────────────────────


class TestMode:
    def test_single_mode(self):
        assert mode([1, 2, 2, 3]) == [2]

    def test_multiple_modes(self):
        assert mode([1, 1, 2, 2, 3]) == [1, 2]

    def test_no_mode(self):
        with pytest.raises(ValueError, match="No mode found"):
            mode([1, 2, 3])

    def test_empty(self):
        with pytest.raises(ValueError):
            mode([])


# ── variance ────────────────────────────────────────────────────────────────


class TestVariance:
    def test_population(self):
        assert variance([2, 4, 4, 4, 5, 5, 7, 9], population=True) == pytest.approx(4.0)

    def test_sample(self):
        result = variance([2, 4, 4, 4, 5, 5, 7, 9], population=False)
        assert result == pytest.approx(4.571428571428571)

    def test_too_few(self):
        with pytest.raises(ValueError):
            variance([1])


# ── std_dev ─────────────────────────────────────────────────────────────────


class TestStdDev:
    def test_population(self):
        assert std_dev([2, 4, 4, 4, 5, 5, 7, 9], population=True) == pytest.approx(2.0)

    def test_sample(self):
        result = std_dev([2, 4, 4, 4, 5, 5, 7, 9], population=False)
        assert result == pytest.approx(math.sqrt(4.571428571428571))


# ── percentile ──────────────────────────────────────────────────────────────


class TestPercentile:
    def test_50th(self):
        assert percentile([1, 2, 3, 4, 5], 50) == 3

    def test_0th(self):
        assert percentile([10, 20, 30], 0) == 10

    def test_100th(self):
        assert percentile([10, 20, 30], 100) == 30

    def test_25th(self):
        assert percentile([1, 2, 3, 4], 25) == pytest.approx(1.75)

    def test_empty(self):
        with pytest.raises(ValueError):
            percentile([], 50)

    def test_out_of_range_low(self):
        with pytest.raises(ValueError):
            percentile([1, 2, 3], -1)

    def test_out_of_range_high(self):
        with pytest.raises(ValueError):
            percentile([1, 2, 3], 101)


# ── z_score ─────────────────────────────────────────────────────────────────


class TestZScore:
    def test_basic(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        result = z_score(5, data)
        assert result == pytest.approx(0.0)

    def test_above_mean(self):
        data = [10, 20, 30]
        result = z_score(30, data)
        assert result > 0

    def test_below_mean(self):
        data = [10, 20, 30]
        result = z_score(10, data)
        assert result < 0

    def test_too_few_points(self):
        with pytest.raises(ValueError):
            z_score(1, [1])

    def test_zero_std_dev(self):
        with pytest.raises(ValueError, match="Standard deviation is zero"):
            z_score(5, [5, 5, 5])


# ── correlation ─────────────────────────────────────────────────────────────


class TestCorrelation:
    def test_perfect_positive(self):
        assert correlation([1, 2, 3], [2, 4, 6]) == pytest.approx(1.0)

    def test_perfect_negative(self):
        assert correlation([1, 2, 3], [6, 4, 2]) == pytest.approx(-1.0)

    def test_length_mismatch(self):
        with pytest.raises(ValueError, match="same length"):
            correlation([1, 2], [1, 2, 3])

    def test_too_few(self):
        with pytest.raises(ValueError):
            correlation([1], [2])

    def test_no_variance(self):
        with pytest.raises(ValueError, match="No variance"):
            correlation([5, 5, 5], [1, 2, 3])

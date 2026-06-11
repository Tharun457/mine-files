"""Basic statistics utilities."""

import math


def mean(data):
    if not data:
        raise ValueError("Cannot compute mean of empty data")
    return sum(data) / len(data)


def median(data):
    if not data:
        raise ValueError("Cannot compute median of empty data")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def mode(data):
    if not data:
        raise ValueError("Cannot compute mode of empty data")
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    if len(modes) == len(counts):
        raise ValueError("No mode found; all values are equally common")
    return sorted(modes)


def variance(data, population=True):
    if len(data) < 2:
        raise ValueError("Need at least 2 data points")
    m = mean(data)
    squared_diffs = [(x - m) ** 2 for x in data]
    if population:
        return sum(squared_diffs) / len(data)
    return sum(squared_diffs) / (len(data) - 1)


def std_dev(data, population=True):
    return math.sqrt(variance(data, population))


def percentile(data, p):
    if not data:
        raise ValueError("Cannot compute percentile of empty data")
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")
    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * (p / 100)
    f = int(k)
    c = f + 1
    if c >= len(sorted_data):
        return sorted_data[f]
    return sorted_data[f] + (k - f) * (sorted_data[c] - sorted_data[f])


def z_score(value, data):
    if len(data) < 2:
        raise ValueError("Need at least 2 data points")
    m = mean(data)
    sd = std_dev(data, population=True)
    if sd == 0:
        raise ValueError("Standard deviation is zero")
    return (value - m) / sd


def correlation(x, y):
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    if len(x) < 2:
        raise ValueError("Need at least 2 data points")
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denom_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    denom_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
    if denom_x == 0 or denom_y == 0:
        raise ValueError("No variance in one or both datasets")
    return numerator / (denom_x * denom_y)

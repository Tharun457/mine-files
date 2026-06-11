# mine-files

A sample Python utility library with five modules covering arithmetic, string manipulation, data validation, file I/O, and statistics.

## Modules

| Module | Description |
|---|---|
| `mine_files.calculator` | Arithmetic operations, factorial, GCD/LCM |
| `mine_files.string_utils` | String reversal, palindrome check, case conversion, truncation |
| `mine_files.validator` | Email, URL, IP, phone, password, and range validation |
| `mine_files.file_handler` | Text/JSON/CSV file I/O, directory listing |
| `mine_files.stats` | Mean, median, mode, variance, percentile, z-score, correlation |

## Running Tests

```bash
pip install pytest pytest-cov
python -m pytest tests/ --cov=mine_files --cov-report=term-missing
```

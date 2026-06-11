"""File I/O and path utilities."""

import os
import json
import csv
from io import StringIO


def read_text(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write_text(filepath, content):
    if not isinstance(content, str):
        raise TypeError("Content must be a string")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def read_json(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(filepath, data, indent=2):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)


def csv_to_dicts(csv_string):
    if not isinstance(csv_string, str):
        raise TypeError("Expected a string")
    reader = csv.DictReader(StringIO(csv_string))
    return list(reader)


def dicts_to_csv(data):
    if not data:
        return ""
    if not isinstance(data, list) or not isinstance(data[0], dict):
        raise TypeError("Expected a list of dicts")
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def get_extension(filepath):
    _, ext = os.path.splitext(filepath)
    return ext.lstrip(".")


def list_files(directory, extension=None):
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Not a directory: {directory}")
    files = []
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            if extension is None or get_extension(full_path) == extension:
                files.append(entry)
    return sorted(files)

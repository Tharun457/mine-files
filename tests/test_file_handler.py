"""Comprehensive tests for the file_handler module."""

import json
import os

import pytest

from mine_files.file_handler import (
    read_text,
    write_text,
    read_json,
    write_json,
    csv_to_dicts,
    dicts_to_csv,
    get_extension,
    list_files,
)


@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path


# ── read_text / write_text ──────────────────────────────────────────────────


class TestReadWriteText:
    def test_round_trip(self, tmp_dir):
        path = str(tmp_dir / "hello.txt")
        write_text(path, "hello world")
        assert read_text(path) == "hello world"

    def test_unicode(self, tmp_dir):
        path = str(tmp_dir / "uni.txt")
        write_text(path, "caf\u00e9 \u2603")
        assert read_text(path) == "caf\u00e9 \u2603"

    def test_read_missing(self):
        with pytest.raises(FileNotFoundError):
            read_text("/nonexistent/path.txt")

    def test_write_bad_content(self, tmp_dir):
        with pytest.raises(TypeError):
            write_text(str(tmp_dir / "bad.txt"), 12345)


# ── read_json / write_json ──────────────────────────────────────────────────


class TestReadWriteJson:
    def test_round_trip(self, tmp_dir):
        path = str(tmp_dir / "data.json")
        data = {"name": "test", "values": [1, 2, 3]}
        write_json(path, data)
        assert read_json(path) == data

    def test_read_missing(self):
        with pytest.raises(FileNotFoundError):
            read_json("/nonexistent/data.json")

    def test_indent(self, tmp_dir):
        path = str(tmp_dir / "indented.json")
        write_json(path, {"a": 1}, indent=4)
        raw = open(path).read()
        assert '    "a": 1' in raw


# ── csv_to_dicts / dicts_to_csv ────────────────────────────────────────────


class TestCsv:
    def test_csv_to_dicts(self):
        csv_str = "name,age\nAlice,30\nBob,25\n"
        result = csv_to_dicts(csv_str)
        assert len(result) == 2
        assert result[0]["name"] == "Alice"
        assert result[1]["age"] == "25"

    def test_csv_to_dicts_type_error(self):
        with pytest.raises(TypeError):
            csv_to_dicts(12345)

    def test_dicts_to_csv(self):
        data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
        result = dicts_to_csv(data)
        assert "name,age" in result
        assert "Alice,30" in result

    def test_dicts_to_csv_empty(self):
        assert dicts_to_csv([]) == ""

    def test_dicts_to_csv_type_error(self):
        with pytest.raises(TypeError):
            dicts_to_csv("not a list")


# ── get_extension ───────────────────────────────────────────────────────────


class TestGetExtension:
    def test_txt(self):
        assert get_extension("file.txt") == "txt"

    def test_double(self):
        assert get_extension("archive.tar.gz") == "gz"

    def test_none(self):
        assert get_extension("Makefile") == ""

    def test_hidden(self):
        assert get_extension(".gitignore") == ""


# ── list_files ──────────────────────────────────────────────────────────────


class TestListFiles:
    def test_list_all(self, tmp_dir):
        (tmp_dir / "a.txt").write_text("a")
        (tmp_dir / "b.py").write_text("b")
        result = list_files(str(tmp_dir))
        assert result == ["a.txt", "b.py"]

    def test_filter_by_extension(self, tmp_dir):
        (tmp_dir / "a.txt").write_text("a")
        (tmp_dir / "b.py").write_text("b")
        result = list_files(str(tmp_dir), extension="py")
        assert result == ["b.py"]

    def test_not_a_directory(self):
        with pytest.raises(NotADirectoryError):
            list_files("/nonexistent/dir")

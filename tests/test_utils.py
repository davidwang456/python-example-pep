"""Tests for utility functions module."""

import os
import tempfile
from pathlib import Path

import pytest

from example_pep import utils


class TestEnsureDir:
    """Tests for ensure_dir function."""

    def test_create_new_directory(self):
        """Test creating new directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            new_dir = os.path.join(tmpdir, "new", "nested", "dir")
            result = utils.ensure_dir(new_dir)
            assert isinstance(result, Path)
            assert result.exists()
            assert result.is_dir()

    def test_existing_directory(self):
        """Test existing directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result1 = utils.ensure_dir(tmpdir)
            result2 = utils.ensure_dir(tmpdir)
            assert result1 == result2
            assert result1.exists()


class TestGetFileSize:
    """Tests for get_file_size function."""

    def test_existing_file(self):
        """Test getting size of existing file."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            content = "test content"
            f.write(content)
            temp_path = f.name

        try:
            size = utils.get_file_size(temp_path)
            assert size == len(content.encode("utf-8"))
        finally:
            os.unlink(temp_path)

    def test_nonexistent_file(self):
        """Test nonexistent file."""
        with pytest.raises(FileNotFoundError):
            utils.get_file_size("/nonexistent/file/path")


class TestSplitPath:
    """Tests for split_path function."""

    def test_unix_path(self):
        """Test Unix path."""
        result = utils.split_path("/usr/local/bin")
        assert "usr" in result
        assert "local" in result
        assert "bin" in result

    def test_relative_path(self):
        """Test relative path."""
        result = utils.split_path("a/b/c")
        assert result == ["a", "b", "c"]

    def test_single_component(self):
        """Test single component."""
        result = utils.split_path("filename")
        assert result == ["filename"]


class TestNormalizePath:
    """Tests for normalize_path function."""

    def test_normalize_relative_path(self):
        """Test normalizing relative path."""
        result = utils.normalize_path(".")
        assert isinstance(result, str)
        assert os.path.isabs(result)

    def test_normalize_absolute_path(self):
        """Test normalizing absolute path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = utils.normalize_path(tmpdir)
            assert result == os.path.abspath(tmpdir)


class TestJoinPaths:
    """Tests for join_paths function."""

    def test_join_multiple_paths(self):
        """Test joining multiple paths."""
        result = utils.join_paths("usr", "local", "bin")
        assert "usr" in result
        assert "local" in result
        assert "bin" in result

    def test_join_single_path(self):
        """Test single path."""
        result = utils.join_paths("usr")
        assert result == "usr"

    def test_join_empty(self):
        """Test empty path."""
        result = utils.join_paths()
        assert result == "."

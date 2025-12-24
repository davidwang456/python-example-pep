"""工具函数模块的测试。"""

import os
import tempfile
from pathlib import Path

import pytest

from python_example_pep import utils


class TestEnsureDir:
    """测试 ensure_dir 函数。"""

    def test_create_new_directory(self):
        """测试创建新目录。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            new_dir = os.path.join(tmpdir, "new", "nested", "dir")
            result = utils.ensure_dir(new_dir)
            assert isinstance(result, Path)
            assert result.exists()
            assert result.is_dir()

    def test_existing_directory(self):
        """测试已存在的目录。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            result1 = utils.ensure_dir(tmpdir)
            result2 = utils.ensure_dir(tmpdir)
            assert result1 == result2
            assert result1.exists()


class TestGetFileSize:
    """测试 get_file_size 函数。"""

    def test_existing_file(self):
        """测试获取已存在文件的大小。"""
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
        """测试不存在的文件。"""
        with pytest.raises(FileNotFoundError):
            utils.get_file_size("/nonexistent/file/path")


class TestSplitPath:
    """测试 split_path 函数。"""

    def test_unix_path(self):
        """测试 Unix 路径。"""
        result = utils.split_path("/usr/local/bin")
        assert "usr" in result
        assert "local" in result
        assert "bin" in result

    def test_relative_path(self):
        """测试相对路径。"""
        result = utils.split_path("a/b/c")
        assert result == ["a", "b", "c"]

    def test_single_component(self):
        """测试单个组件。"""
        result = utils.split_path("filename")
        assert result == ["filename"]


class TestNormalizePath:
    """测试 normalize_path 函数。"""

    def test_normalize_relative_path(self):
        """测试规范化相对路径。"""
        result = utils.normalize_path(".")
        assert isinstance(result, str)
        assert os.path.isabs(result)

    def test_normalize_absolute_path(self):
        """测试规范化绝对路径。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            result = utils.normalize_path(tmpdir)
            assert result == os.path.abspath(tmpdir)


class TestJoinPaths:
    """测试 join_paths 函数。"""

    def test_join_multiple_paths(self):
        """测试连接多个路径。"""
        result = utils.join_paths("usr", "local", "bin")
        assert "usr" in result
        assert "local" in result
        assert "bin" in result

    def test_join_single_path(self):
        """测试单个路径。"""
        result = utils.join_paths("usr")
        assert result == "usr"

    def test_join_empty(self):
        """测试空路径。"""
        result = utils.join_paths()
        assert result == "."


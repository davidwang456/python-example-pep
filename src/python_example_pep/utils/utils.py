"""工具函数模块。"""

import os
from pathlib import Path
from typing import List, Optional


def ensure_dir(path: str) -> Path:
    """
    确保目录存在，如果不存在则创建。

    Args:
        path: 目录路径

    Returns:
        Path 对象

    Raises:
        OSError: 如果无法创建目录
    """
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def get_file_size(file_path: str) -> int:
    """
    获取文件大小（字节）。

    Args:
        file_path: 文件路径

    Returns:
        文件大小（字节）

    Raises:
        FileNotFoundError: 如果文件不存在
        OSError: 如果无法访问文件
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    return os.path.getsize(file_path)


def split_path(path: str) -> List[str]:
    """
    分割路径为各个组成部分。

    Args:
        path: 文件或目录路径

    Returns:
        路径组成部分的列表

    Examples:
        >>> split_path("/usr/local/bin")
        ['usr', 'local', 'bin']
        >>> split_path("C:\\Windows\\System32")
        ['C:', 'Windows', 'System32']
    """
    parts = []
    current = Path(path)
    while current != current.parent:
        parts.insert(0, current.name)
        current = current.parent
    if current.anchor:
        parts.insert(0, current.anchor.rstrip(os.sep))
    return [p for p in parts if p]


def normalize_path(path: str) -> str:
    """
    规范化路径字符串。

    Args:
        path: 原始路径

    Returns:
        规范化后的路径
    """
    return str(Path(path).resolve())


def join_paths(*paths: str) -> str:
    """
    连接多个路径。

    Args:
        *paths: 要连接的路径部分

    Returns:
        连接后的路径

    Examples:
        >>> join_paths("usr", "local", "bin")
        'usr/local/bin'
    """
    return str(Path(*paths))


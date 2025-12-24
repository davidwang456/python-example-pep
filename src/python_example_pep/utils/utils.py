"""Utility functions module."""

import os
from pathlib import Path
from typing import List, Optional


def ensure_dir(path: str) -> Path:
    """
    Ensure directory exists, create if it doesn't.

    Args:
        path: Directory path

    Returns:
        Path object

    Raises:
        OSError: If directory cannot be created
    """
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def get_file_size(file_path: str) -> int:
    """
    Get file size in bytes.

    Args:
        file_path: File path

    Returns:
        File size in bytes

    Raises:
        FileNotFoundError: If file does not exist
        OSError: If file cannot be accessed
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return os.path.getsize(file_path)


def split_path(path: str) -> List[str]:
    """
    Split path into its components.

    Args:
        path: File or directory path

    Returns:
        List of path components

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
    Normalize path string.

    Args:
        path: Original path

    Returns:
        Normalized path
    """
    return str(Path(path).resolve())


def join_paths(*paths: str) -> str:
    """
    Join multiple paths.

    Args:
        *paths: Path parts to join

    Returns:
        Joined path

    Examples:
        >>> join_paths("usr", "local", "bin")
        'usr/local/bin'
    """
    return str(Path(*paths))


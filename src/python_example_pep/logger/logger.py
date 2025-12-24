"""Logging module."""

import logging
import sys
from enum import Enum
from pathlib import Path
from typing import Optional


class LogLevel(Enum):
    """Log level enumeration."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class Logger:
    """Logger class."""

    def __init__(
        self,
        name: str,
        level: LogLevel = LogLevel.INFO,
        log_file: Optional[str] = None,
    ):
        """
        Initialize logger.

        Args:
            name: Logger name
            level: Log level
            log_file: Log file path (optional)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level.value)
        self.logger.handlers.clear()

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level.value)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # File handler (if specified)
        if log_file:
            file_path = Path(log_file)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(level.value)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        """
        Log DEBUG level message.

        Args:
            message: Log message
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Log INFO level message.

        Args:
            message: Log message
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Log WARNING level message.

        Args:
            message: Log message
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Log ERROR level message.

        Args:
            message: Log message
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Log CRITICAL level message.

        Args:
            message: Log message
        """
        self.logger.critical(message)

    def set_level(self, level: LogLevel) -> None:
        """
        Set log level.

        Args:
            level: New log level
        """
        self.logger.setLevel(level.value)
        for handler in self.logger.handlers:
            handler.setLevel(level.value)


def get_logger(name: str, level: LogLevel = LogLevel.INFO) -> Logger:
    """
    Get logger instance.

    Args:
        name: Logger name
        level: Log level

    Returns:
        Logger instance
    """
    return Logger(name, level)


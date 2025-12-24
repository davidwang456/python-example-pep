"""Tests for logging module."""

import logging
import tempfile
from pathlib import Path

import pytest

from python_example_pep import logger


class TestLogLevel:
    """Tests for LogLevel enumeration."""

    def test_log_levels(self):
        """Test log level values."""
        assert logger.LogLevel.DEBUG.value == logging.DEBUG
        assert logger.LogLevel.INFO.value == logging.INFO
        assert logger.LogLevel.WARNING.value == logging.WARNING
        assert logger.LogLevel.ERROR.value == logging.ERROR
        assert logger.LogLevel.CRITICAL.value == logging.CRITICAL


class TestLogger:
    """Tests for Logger class."""

    def test_logger_initialization(self):
        """Test logger initialization."""
        log = logger.Logger("test_logger")
        assert log.logger.name == "test_logger"
        assert len(log.logger.handlers) > 0

    def test_logger_with_file(self):
        """Test logger with file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = str(Path(tmpdir) / "test.log")
            log = logger.Logger("test_logger", log_file=log_file)
            log.info("test message")
            assert Path(log_file).exists()
            # Close all handlers to release file handles (required on Windows)
            for handler in log.logger.handlers:
                handler.close()

    def test_debug(self, caplog):
        """Test DEBUG level logging."""
        log = logger.Logger("test", level=logger.LogLevel.DEBUG)
        with caplog.at_level(logging.DEBUG):
            log.debug("debug message")
            assert "debug message" in caplog.text

    def test_info(self, caplog):
        """Test INFO level logging."""
        log = logger.Logger("test", level=logger.LogLevel.INFO)
        with caplog.at_level(logging.INFO):
            log.info("info message")
            assert "info message" in caplog.text

    def test_warning(self, caplog):
        """Test WARNING level logging."""
        log = logger.Logger("test", level=logger.LogLevel.WARNING)
        with caplog.at_level(logging.WARNING):
            log.warning("warning message")
            assert "warning message" in caplog.text

    def test_error(self, caplog):
        """Test ERROR level logging."""
        log = logger.Logger("test", level=logger.LogLevel.ERROR)
        with caplog.at_level(logging.ERROR):
            log.error("error message")
            assert "error message" in caplog.text

    def test_critical(self, caplog):
        """Test CRITICAL level logging."""
        log = logger.Logger("test", level=logger.LogLevel.CRITICAL)
        with caplog.at_level(logging.CRITICAL):
            log.critical("critical message")
            assert "critical message" in caplog.text

    def test_set_level(self):
        """Test setting log level."""
        log = logger.Logger("test", level=logger.LogLevel.INFO)
        log.set_level(logger.LogLevel.DEBUG)
        assert log.logger.level == logging.DEBUG


class TestGetLogger:
    """Tests for get_logger function."""

    def test_get_logger(self):
        """Test getting logger."""
        log = logger.get_logger("test_logger")
        assert isinstance(log, logger.Logger)
        assert log.logger.name == "test_logger"

    def test_get_logger_with_level(self):
        """Test logger with level."""
        log = logger.get_logger("test", level=logger.LogLevel.DEBUG)
        assert log.logger.level == logging.DEBUG

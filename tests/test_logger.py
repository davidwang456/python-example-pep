"""日志记录模块的测试。"""

import logging
import tempfile
from pathlib import Path

import pytest

from python_example_pep import logger


class TestLogLevel:
    """测试 LogLevel 枚举。"""

    def test_log_levels(self):
        """测试日志级别值。"""
        assert logger.LogLevel.DEBUG.value == logging.DEBUG
        assert logger.LogLevel.INFO.value == logging.INFO
        assert logger.LogLevel.WARNING.value == logging.WARNING
        assert logger.LogLevel.ERROR.value == logging.ERROR
        assert logger.LogLevel.CRITICAL.value == logging.CRITICAL


class TestLogger:
    """测试 Logger 类。"""

    def test_logger_initialization(self):
        """测试日志记录器初始化。"""
        log = logger.Logger("test_logger")
        assert log.logger.name == "test_logger"
        assert len(log.logger.handlers) > 0

    def test_logger_with_file(self):
        """测试带文件的日志记录器。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = str(Path(tmpdir) / "test.log")
            log = logger.Logger("test_logger", log_file=log_file)
            log.info("test message")
            assert Path(log_file).exists()
            # 关闭所有处理器以释放文件句柄（Windows 需要）
            for handler in log.logger.handlers:
                handler.close()

    def test_debug(self, caplog):
        """测试 DEBUG 级别日志。"""
        log = logger.Logger("test", level=logger.LogLevel.DEBUG)
        with caplog.at_level(logging.DEBUG):
            log.debug("debug message")
            assert "debug message" in caplog.text

    def test_info(self, caplog):
        """测试 INFO 级别日志。"""
        log = logger.Logger("test", level=logger.LogLevel.INFO)
        with caplog.at_level(logging.INFO):
            log.info("info message")
            assert "info message" in caplog.text

    def test_warning(self, caplog):
        """测试 WARNING 级别日志。"""
        log = logger.Logger("test", level=logger.LogLevel.WARNING)
        with caplog.at_level(logging.WARNING):
            log.warning("warning message")
            assert "warning message" in caplog.text

    def test_error(self, caplog):
        """测试 ERROR 级别日志。"""
        log = logger.Logger("test", level=logger.LogLevel.ERROR)
        with caplog.at_level(logging.ERROR):
            log.error("error message")
            assert "error message" in caplog.text

    def test_critical(self, caplog):
        """测试 CRITICAL 级别日志。"""
        log = logger.Logger("test", level=logger.LogLevel.CRITICAL)
        with caplog.at_level(logging.CRITICAL):
            log.critical("critical message")
            assert "critical message" in caplog.text

    def test_set_level(self):
        """测试设置日志级别。"""
        log = logger.Logger("test", level=logger.LogLevel.INFO)
        log.set_level(logger.LogLevel.DEBUG)
        assert log.logger.level == logging.DEBUG


class TestGetLogger:
    """测试 get_logger 函数。"""

    def test_get_logger(self):
        """测试获取日志记录器。"""
        log = logger.get_logger("test_logger")
        assert isinstance(log, logger.Logger)
        assert log.logger.name == "test_logger"

    def test_get_logger_with_level(self):
        """测试带级别的日志记录器。"""
        log = logger.get_logger("test", level=logger.LogLevel.DEBUG)
        assert log.logger.level == logging.DEBUG


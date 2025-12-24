"""日志记录模块。"""

import logging
import sys
from enum import Enum
from pathlib import Path
from typing import Optional


class LogLevel(Enum):
    """日志级别枚举。"""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class Logger:
    """日志记录器类。"""

    def __init__(
        self,
        name: str,
        level: LogLevel = LogLevel.INFO,
        log_file: Optional[str] = None,
    ):
        """
        初始化日志记录器。

        Args:
            name: 日志记录器名称
            level: 日志级别
            log_file: 日志文件路径（可选）
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level.value)
        self.logger.handlers.clear()

        # 创建格式化器
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # 控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level.value)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # 文件处理器（如果指定）
        if log_file:
            file_path = Path(log_file)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(level.value)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        """
        记录 DEBUG 级别日志。

        Args:
            message: 日志消息
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        记录 INFO 级别日志。

        Args:
            message: 日志消息
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        记录 WARNING 级别日志。

        Args:
            message: 日志消息
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        记录 ERROR 级别日志。

        Args:
            message: 日志消息
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        记录 CRITICAL 级别日志。

        Args:
            message: 日志消息
        """
        self.logger.critical(message)

    def set_level(self, level: LogLevel) -> None:
        """
        设置日志级别。

        Args:
            level: 新的日志级别
        """
        self.logger.setLevel(level.value)
        for handler in self.logger.handlers:
            handler.setLevel(level.value)


def get_logger(name: str, level: LogLevel = LogLevel.INFO) -> Logger:
    """
    获取日志记录器实例。

    Args:
        name: 日志记录器名称
        level: 日志级别

    Returns:
        Logger 实例
    """
    return Logger(name, level)


"""
This module provides a utility function to set up a logger with both console output and optional file logging.
"""

import logging
import logging.handlers
import sys
from pathlib import Path
from typing import Literal

log_mapper = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "CRITICAL": logging.CRITICAL,
}


def setup_logger(
    name: str = "app",
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO",
    log_file: Path | None = None,
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB per file
    backup_count: int = 5,
) -> logging.Logger:
    """
    Setup a logger with console + optional file rotation.

    Args:
        name: Logger name (use __name__ in modules).
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR).
        log_file: If provided, logs will also be written to this file.
        max_bytes: Max size of a log file before rotation.
        backup_count: Number of rotated files to keep.

    Returns:
        Configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_mapper.get(log_level, logging.INFO))

    # Avoid duplicate handlers if logger already set up
    if logger.handlers:
        return logger

    # Formatter with timestamp, level, and module
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler with rotation
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

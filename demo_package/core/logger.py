"""Logging utilities."""

import datetime


def setup_logger(name: str, level: str = "INFO") -> None:
    """Set up a logger with the given name and level."""
    # Feature B: add timestamp to setup message
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] Setting up logger: {name} at level {level}")


def log_info(message: str) -> None:
    """Log an info message."""
    # Feature B: add timestamp to log messages
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] INFO: {message}")


def log_error(message: str) -> None:
    """Log an error message."""
    # Feature B: add timestamp to log messages
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] ERROR: {message}")


def log_warning(message: str) -> None:
    """Log a warning message."""
    # Feature B: new warning log function
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] WARNING: {message}")

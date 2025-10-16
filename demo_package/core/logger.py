"""Logging utilities."""


def setup_logger(name: str, level: str = "INFO") -> None:
    """Set up a logger with the given name and level."""
    print(f"Setting up logger: {name} at level {level}")


def log_info(message: str) -> None:
    """Log an info message."""
    print(f"INFO: {message}")


def log_error(message: str) -> None:
    """Log an error message."""
    print(f"ERROR: {message}")

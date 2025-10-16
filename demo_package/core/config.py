"""Configuration module."""

from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration."""

    name: str
    version: str
    debug: bool = False


def get_default_config() -> Config:
    """Get the default configuration."""
    return Config(name="demo", version="0.1.0", debug=False)


def load_config(config_path: str) -> Config:
    """Load configuration from a file."""
    # Dummy implementation
    return Config(name="demo", version="0.1.0", debug=True)

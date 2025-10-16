"""Data processing algorithms."""

from demo_package.core.config import Config, get_default_config
from demo_package.core.logger import log_info


def process_data(data: list[int], config: Config | None = None) -> list[int]:
    """Process data using the given configuration."""
    if config is None:
        config = get_default_config()

    log_info(f"Processing {len(data)} items with config: {config.name}")

    # Dummy processing: multiply each item by 2
    return [x * 2 for x in data]


def validate_data(data: list[int]) -> bool:
    """Validate that data meets requirements."""
    log_info(f"Validating {len(data)} items")
    return len(data) > 0 and all(isinstance(x, int) for x in data)

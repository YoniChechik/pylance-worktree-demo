"""API endpoints."""

from demo_package.algo.analyzer import analyze_data
from demo_package.algo.processor import process_data
from demo_package.core.config import Config, load_config
from demo_package.core.logger import log_info, setup_logger


def initialize_api(config_path: str) -> Config:
    """Initialize the API with the given configuration."""
    setup_logger("api", level="DEBUG")
    config = load_config(config_path)
    log_info(f"API initialized with config: {config.name}")
    return config


def handle_process_request(data: list[int]) -> dict[str, list[int]]:
    """Handle a data processing request."""
    log_info(f"Received process request with {len(data)} items")
    processed = process_data(data)
    return {"processed": processed}


def handle_analyze_request(data: list[int]) -> dict[str, dict[str, int | float]]:
    """Handle a data analysis request."""
    log_info(f"Received analyze request with {len(data)} items")
    stats = analyze_data(data)
    return {"statistics": stats}

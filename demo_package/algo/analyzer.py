"""Data analysis module."""

from demo_package.algo.processor import process_data, validate_data
from demo_package.core.logger import log_error, log_info


def analyze_data(data: list[int]) -> dict[str, int | float]:
    """Analyze data and return statistics."""
    if not validate_data(data):
        log_error("Invalid data provided")
        return {}

    processed = process_data(data)
    log_info(f"Analyzed {len(processed)} processed items")

    return {
        "count": len(processed),
        "sum": sum(processed),
        "mean": sum(processed) / len(processed),
        "max": max(processed),
        "min": min(processed),
    }

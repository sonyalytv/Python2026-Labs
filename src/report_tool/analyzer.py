"""
Provides helper functions for parsing and analyzing numeric data.
"""
import logging

logger = logging.getLogger(__name__)

def _cleanup_pieces(parts: list[str]) -> list[str]:
    cleaned = []
    for item in parts:
        item = item.strip()
        if item != "":
            cleaned.append(item)
    return cleaned

def parse_numbers(text: str) -> list[float]:
    logger.debug(f"Parsing raw text for numbers.")
    pieces = text.replace(";", ",").split(",")
    pieces = _cleanup_pieces(pieces)
    result = []

    for p in pieces:
        result.append(float(p))

    logger.info(f"Successfully parsed {len(result)} numbers.")
    return result

def _check_input(numbers: list[float]) -> None:
    if not numbers:
        logger.error("Empty input provided for analysis.")
        raise ValueError("numbers must not be empty")

def analyze_numbers(numbers: list[float]) -> dict[str, float]:
    logger.debug("Running statistical analysis on numbers.")
    _check_input(numbers)

    total = sum(numbers)
    count = len(numbers)
    avg = total / count

    logger.info("Analysis complete.")
    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": avg,
    }

def _sort_numbers(numbers: list[float]) -> list[float]:
    return sorted(numbers)

if __name__ == "__main__":
    print("Module: analyzer")
    print("Purpose: Parses text into numeric lists and computes basic statistics.")
    print("Public Functions: parse_numbers, analyze_numbers")
    print('Example: analyze_numbers([1.0, 2.0, 3.0])')
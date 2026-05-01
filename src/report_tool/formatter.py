"""
Handles the formatting of analyzed statistics into textual and JSON reports.
"""
import json
import logging
from typing import Any
from .analyzer import _sort_numbers

logger = logging.getLogger(__name__)

def _line_maker(name: str, value: Any) -> str:
    return f"{name}: {value}"

def _pretty_title(text: str) -> str:
    return text.strip().title()

def build_report(stats: dict[str, float]) -> str:
    logger.debug("Building standard text report")
    lines = []
    lines.append(_pretty_title("number report"))
    lines.append("-" * 20)
    lines.append(_line_maker("count", stats["count"]))
    lines.append(_line_maker("sum", stats["sum"]))
    lines.append(_line_maker("min", stats["min"]))
    lines.append(_line_maker("max", stats["max"]))
    lines.append(_line_maker("mean", round(stats["mean"], 2)))
    return "\n".join(lines)

def build_sorted_report(numbers: list[float], stats: dict[str, float]) -> str:
    logger.debug("Building sorted text report")
    ordered = _sort_numbers(numbers)

    lines = []
    lines.append(_pretty_title("number report"))
    lines.append("-" * 20)
    lines.append(_line_maker("count", stats["count"]))
    lines.append(_line_maker("sum", stats["sum"]))
    lines.append(_line_maker("min", stats["min"]))
    lines.append(_line_maker("max", stats["max"]))
    lines.append(_line_maker("mean", round(stats["mean"], 2)))
    lines.append(_line_maker("sorted", ordered))
    return "\n".join(lines)

def build_json_report(stats: dict[str, float]) -> str:
    logger.debug("Building standard JSON report")
    return json.dumps(stats, indent=4)

def build_sorted_json_report(numbers: list[float], stats: dict[str, float]) -> str:
    logger.debug("Building sorted JSON report")
    ordered = _sort_numbers(numbers)
    
    data: dict[str, Any] = dict(stats)
    data["sorted"] = ordered
    return json.dumps(data, indent=4)

def _internal_banner() -> str:
    return "=" * 30

if __name__ == "__main__":
    print("Module: formatter")
    print("Purpose: Formats analyzed data into clean textual or JSON reports.")
    print("Public Functions: build_report, build_sorted_report, build_json_report, build_sorted_json_report")
    print('Example: build_json_report({"count": 3, "sum": 12, "min": 2, "max": 6, "mean": 4})')
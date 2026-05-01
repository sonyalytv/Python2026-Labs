"""
Handles reading data from inputs and saving reports to the filesystem using pathlib.
"""
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def read_input(filepath: str) -> str:
    logger.info(f"Reading input data from: {filepath}")
    path = Path(filepath)
    if not path.is_file():
        logger.error(f"Input file not found: {filepath}")
        raise FileNotFoundError(f"Cannot find input file: {filepath}")
    return path.read_text(encoding="utf-8")

def save_report(report: str, filepath: str) -> str:
    logger.info(f"Saving report to: {filepath}")
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    return str(path)

def read_back(filepath: str) -> str:
    logger.debug(f"Reading back report data from: {filepath}")
    return Path(filepath).read_text(encoding="utf-8")

if __name__ == "__main__":
    print("Module: storage")
    print("Purpose: Safely reads and saves file contents.")
    print("Public Functions: save_report, read_back, read_input")
    print('Example: save_report("My Report", "output.txt")')
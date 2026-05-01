# Lab 10 Report

## 1. What was added
Several major capabilities were introduced to upgrade the project into a fully-fledged CLI application:
* **CLI Interface:** Utilizing the `argparse` module, the main execution script now accepts dynamic arguments (`--input`, `--out`, `--format`, `--log-level`) instead of relying on hardcoded logic.
* **File Input/Output:** The `pathlib` standard library was integrated into the `storage.py` module to robustly handle the reading of input data streams and safely writing output reports.
* **JSON Output:** The `formatter.py` module was expanded to support JSON generation alongside standard text generation using the `json` library, allowing dual-format processing.
* **Logging:** The `logging` module replaced standard console prints. Controlled logging events were added throughout the pipeline modules (`analyzer`, `formatter`, `storage`) to track reading, parsing, analysis, and writing steps.

## 2. How the tool changed
The tool evolved drastically from a **demo-style execution** to **real CLI-based usage**. 
Previously, the `__main__.py` ran a hardcoded "example workflow" which ignored external data entirely. Users had to edit the source code to analyze new numbers. Now, the main module serves strictly as an orchestrator for the command line. It delegates dynamic input files, selects standard workflows based on user flags, tracks progress via logs, and deposits the results dynamically into user-specified output locations. Module responsibilities were entirely preserved, ensuring the code remains clean and modular.

## 3. Why these changes matter
* **CLI improves usability and automation:** A command-line interface allows users and external systems (like bash scripts or cron jobs) to pass dynamic inputs without ever touching the source code.
* **JSON is useful for machine-readable output:** Providing a structured format like JSON enables seamless integration with other software tools, APIs, and databases that require strict data ingestion formats instead of text scraping.
* **Logging improves debugging and transparency:** Standard print statements clutter the user's terminal and don't provide severity tracking. The logging module isolates program output (the report) from execution traces (the logs), granting users control over the verbosity via log levels for deep debugging or silent execution.
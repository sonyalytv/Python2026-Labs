# Report Tool

A Python CLI tool for parsing, analyzing, and formatting numeric reports.

## What it does
The Report Tool allows you to read raw text strings containing numbers from an input file, convert them into usable data, generate statistical summaries (count, sum, min, max, mean), and safely output those summaries into either text or JSON format. It features adjustable logging to track execution progress without cluttering the final output.

## CLI Arguments
The tool relies on a command-line interface rather than hardcoded variables. Supported arguments include:
* `--input`: (Required) The path to the file containing the raw numeric data.
* `--out`: (Required) The path where the generated report should be saved.
* `--format`: (Optional) Choose between `text` or `json`. Defaults to `text`.
* `--log-level`: (Optional) Choose the verbosity of execution logs (`DEBUG`, `INFO`, `WARNING`, `ERROR`). Defaults to `INFO`.

## Output Formats
* **Text (`text`)**: Produces a human-readable text file formatted with basic borders and clearly labeled statistics.
* **JSON (`json`)**: Produces a structured, machine-readable JSON object representing the exact same analysis, ideal for integration with other tools.

## How to run it
Recommended Python version is `Python 3.12.6`.

Open `lab10/` and run the following to setup the environment:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
If environment activation fails try running:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
You can run the tool as a complete package to see its capabilities and a demonstration workflow:
```bash
cd src/
python -m report_tool
```
Example: *Generating a standard text report with INFO logging:*
```bash
cd src/
python -m report_tool --input ../data.txt --out ../report.txt --format text --log-level INFO
```
Example: *Generating a JSON report with WARNING logging:*
```bash
cd src/
python -m report_tool --input ../data.txt --out ../report.json --format json --log-level WARNING
```
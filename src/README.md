# Report Tool

A Python tool for parsing, analyzing, and formatting numeric reports.

## What it does
The Report Tool allows you to take raw text strings containing numbers, convert them into usable data, generate statistical summaries (count, sum, min, max, mean), and format those summaries into clean text reports.

## How to run it
Recommended Python version is `Python 3.12.6`.

Open `lab08/` and run the following to setup the environment:
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
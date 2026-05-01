# LAB10: Command-Line Report Tool

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Task A](#task-a--command-line-interface)
- [Task B](#task-b--file-based-workflow)
- [Task C](#task-c--multiple-output-formats)
- [Task D](#task-d--controlled-logging)
- [Task E](#task-e--clean-integration-with-existing-package)

## Goal
Extend your existing report tool so that it can be used as a real command-line tool that reads input data from files, processes it using your existing logic, produces output in different formats, and provides controlled logging of its execution.

The focus of this lab is on:
* CLI design (`argparse`)
* file handling (`pathlib`)
* structured data (`json`)
* logging (`logging`)
* integration with an existing codebase

## Lab Structure
```
lab10/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ report.md
│
└─ src/
    ├─ README.md
    └─ tasks/
        ├─ __init__.py
        ├─ __main__.py
        ├─ analyzer.py
        ├─ formatter.py
        └─ storage.py
```

## Getting Started
Recommended Python version is `Python 3.12.6`.

Open `lab010/` and run the following to setup the environment:
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
python -m src.report_tool
```
You can also run each induvidual module:
```bash
python -m src.report_tool.analyzer
python -m src.report_tool.formatter
python -m src.report_tool.storage
```
Test passing strict type checking:
```bash
mypy --strict .
```


### Task A $-$ Command-line interface
The tool must support the following command format:
```bash
python -m report_tool --input <file> --out <file> --format text|json --log-level DEBUG|INFO|WARNING|ERROR
```
* All arguments must be handled through a command-line interface.
* The program must not require code modification to change input, output, or format.

### Task B $-$ File-based workflow
The tool must:
* read numeric data from an input file;
* process it using the existing pipeline (parse -> analyze -> format); 
* write the result to the specified output file.
* File handling must be implemented in a clear and reliable way. 


### Task C $-$ Multiple output formats
The tool must support two output formats:

* `text`: human-readable report (based on your existing formatting logic).
* `json`: structured output based on analysis results.
* Both formats must be generated from the same analysis result, not from each other.


### Task D $-$ Controlled logging
The tool must use logging to report its execution.
* log the main steps of the pipeline (reading input, parsing, analysis, writing output);
* do not mix logging output with the main program output;
* support user-controlled logging level via: `--log-level DEBUG|INFO|WARNING|ERROR`.


### Task E $-$ Clean integration with existing package
The new functionality must:
* be integrated into the existing report tool structure;
* preserve module responsibilities from Lab 09;
* not move all logic into a single file;
* keep the package-level API meaningful and usable.
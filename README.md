# LAB09: Repairing a Broken Python Project

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Task A](#task-a--clean-project-shape)
- [Task B](#task-b--public-vs-private-design)
- [Task C](#task-c--execution-behaviour)
- [Task D](#task-d--package-level-api)
- [Task E](#task-e--stable-usage)

## Goal
Transform the given project into a clean, structured, and usable Python tool.

The focus of this lab is not on algorithms, but on:
*  project structure 
* modules and packages 
* imports 
* public vs private API 
* reproducible usage 

## Lab Structure
```
lab09/
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


### Task A $-$ Clean project shape
The project should have:
* a clear and coherent structure; 
* meaningful module names; 
* no leftover debugging or testing code inside modules; 
* a cleaned `requirements.txt` reflecting actual dependencies; 
* a concise and usable `README.md` explaining: 
    * what the tool does, 
    * how to run it, 
    * how to use it.


### Task B $-$ Public vs private design
The project should have:
* meaningful function names; 
* a clear distinction between public and internal functions; 
* internal functions marked using underscore (`_`) convention; 
* a consistent and intentional public API. 


### Task C $-$ Execution behaviour
The project must behave as follows:

*Running the tool as a package*
```bash
python -m report_tool
```
Should produce:
* a short description of the tool; 
* a list of its main public capabilities; 
* minimal usage instructions; 
* one or more examples. 

*Running individual modules*

Each module should be runnable and should:
* describe its purpose; 
* list its public functions; 
* show minimal usage examples. 


### Task D $-$ Package-level API
Public functions must be importable directly from the package:
```bash
from report_tool import ...
```
* Internal functions should not appear as part of the public API. 
* The package API should be clean and predictable.


### Task E $-$ Stable usage
The project should be stable and predictable to use:
* no path hacks (e.g., no `sys.path.append`); 
* consistent execution model; 
* documentation matches actual behavior; 
* another developer should be able to run and use the tool without guessing.
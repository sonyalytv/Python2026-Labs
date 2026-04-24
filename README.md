# LAB08: Iteration, Context Managers, and Descriptors

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--iteration)
- [Task B](#task-b--context-manager)
- [Task C](#task-c--descriptor)
- [Task D](#task-d--integration)

## Goal
In this lab we implement a custom object that integrates with Python through several core protocols.

We work with a collection of students and extend it step by step so that it:
* can be used in a `for` loop (iteration protocol)
* can be used in a `with` statement (context manager protocol)
* validates attribute access (descriptor)

The goal is to understand that Python behavior is driven by protocols implemented via special methods.

## Lab Structure
```
lab08/
├─ README.md
├─ requirements.txt
├─ runme.bat
│
├─ report/
│   └─ answers.md
│
└─ src/
    ├─ lab08.py
    ├─ tasks/
    │   ├─ __init__.py
    │   ├─ task_a.py
    │   ├─ task_b.py
    │   ├─ task_c.py
    │   └─ task_d.py
    └─ utils/
        ├─ __init__.py
        └─ utils.py
```

## Getting Started
For simple and fast lab execution, double click `runme.bat` file to run it.

To work directly with the code, follow the instructions below.

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
Command to run the program:
```bash
python src/lab08.py
```
Test passing strict type checking:
```bash
mypy --strict .
```

## Output Structure
The program prints four sections (A–D), each demonstrating a specific concepts, extending a created collection step-by-step: iteration protocols, context manager protocols, descriptors.

### Task A $-$ Iteration
Created a class `StudentCollection` that can store multiple students. Implemented `__iter__` and `__next__` dunders to make it iterable.

### Task B $-$ Context Manager
Extended the `StudentCollection` class so that it could act as a context by implementing `__enter__` and `__exit__` methods.

### Task C $-$ Descriptor
Created a descriptor to validate student grades. As a result, invalid values get rejected.

### Task D $-$ Integration
Demonstrated how all the components can be used together.
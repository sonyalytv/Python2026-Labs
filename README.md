# LAB07: Behavior, Protocols, ABC, Dataclasses, Slots

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--regular-class-duck-typing)
- [Task B](#task-b--dataclass-implementation)
- [Task C](#task-c--slots)
- [Task D](#task-d--abc-version)

## Goal
In this lab we explore different ways to define and implement behavior in Python.

We work with a single concept $-$ an object that can be serialized $-$ and implement it using different approaches:
Students should demonstrate understanding of:
* duck typing (regular class)
* Protocol (structural typing)
* dataclass
* slots
* Abstract Base Classes (ABC)

The goal is to understand how Python defines "type" through behavior rather than inheritance.

## Lab Structure
```
lab07/
├─ README.md
├─ requirements.txt
├─ runme.bat
│
├─ report/
│   └─ answers.md
│
└─ src/
    ├─ lab07.py
    └─ tasks/
        ├─ __init__.py
        ├─ task_a.py
        ├─ task_b.py
        ├─ task_c.py
        └─ task_d.py
    └─ utils/
        ├─ __init__.py
        ├─ preparation.py
        └─ utils.py
```

## Getting Started
For simple and fast lab execution, double click `runme.bat` file to run it.

To work directly with the code, follow the instructions below.

Recommended Python version is `Python 3.12.6`.

Open `lab07/` and run the following to setup the environment:
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
python src/lab07.py
```
Test passing strict type checking:
```bash
mypy --strict .
```

## Output Structure
The program prints four sections (A–D), each demonstrating a specific approach to creating an object: regular classes, Protocols, dataclasses, slots, Abstract Base Classes.

### Task A $-$ Regular class (duck typing)
Implemented a regular class `StudentRegular` which doesn't inherit from anything. It still works with the general Protocol of `Serializable` object. It demonstrates duck typing.

### Task B $-$ Dataclass implementation
Utilized `dataclass` to create a dataclass version of the student class $-$ `StudentData`. The code is easier to read, the behavior is the same as in Task A, the object is fully compatible with the Protocol.

### Task C $-$ Slots
Created a dataclass with slots $-$ `StudentSlots`. The Protocol works, the object structure is now restricted, and its internal storage differs from regular objects.

### Task D $-$ ABC version
Used an abstract base class (ABC) and implemented `StudentABC` to get the same behavior as in the previous tasks. Showed that ABC requires inheritance, unlike Protocol.
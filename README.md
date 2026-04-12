# LAB06: Python Object Model and Basic Object Behavior

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--define-the-student-class)
- [Task B](#task-b--inspect-internal-structure)
- [Task C](#task-c--implement-__str__)
- [Task D](#task-d--implement-__repr__)
- [Task E](#task-e--implement-equality-__eq__)
- [Task F](#task-f--implement-ordering-__lt__)
- [Task G](#task-g--sorting)

## Goal
In this lab a custom Python class is implemented and gradually transformed into a well-behaved object that integrates with the language. The goal of this lab is to practice:

* working with classes and objects
* understanding how attributes are stored
* implementing basic dunder methods
* controlling object behavior in Python
* writing type-safe code with `mypy --strict`

## Lab Structure
```
lab06/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ answers.md
│
└─ src/
    ├─ lab06.py
    ├─ student.py
    └─ utils.py
```

## Getting Started
Recommended Python version is `Python 3.12.6`.

Open `lab06/` and run the following to setup the environment:
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
python src/lab06.py
```
Test passing strict type checking:
```bash
mypy --strict src/lab06.py
```

## Output Structure
The program prints seven sections (A–G), each demonstrating a specific concept: classes in Python, attributes, dunder methods, and controlling object behavior.

### Task A $-$ Define the `Student` class
Created a `Student` class with `name`, `group`, `average_float` attributes, and initialized them via `__init__`.

### Task B $-$ Inspect internal structure
Demonstrated how attributes are stored inside the object.

### Task C $-$ Implement `__str__`
Defined a user-friendly string representation by implementing an `__str__` dunder.

### Task D $-$ Implement `__repr__`
Defined a developer-oriented representation by implementing a `__repr__` dunder.

### Task E $-$ Implement equality (`__eq__`)
Implemented an `__eq__` dunder to check the equality of two objects of the same class.

### Task F $-$ Implement ordering (`__lt__`)
Implemented an `__lt__` dunder to compare two objects of the same class.

### Task G $-$ Sorting
Demonstrated that the created objects integrate with Python: can be sorted by `average_grade` attribute and printed in a user-friendly way.
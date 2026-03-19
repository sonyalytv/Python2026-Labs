# LAB02: Expressions & Control Flow in Python

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--truthiness)
- [Task B](#task-b--identity-vs-equality)
- [Task C](#task-c--control-flow)
- [Task D](#task-d--pattern-matching)
- [Task E](#task-e--comprehensions)
- [Task F](#task-f--generators)

## Goal
The goal of this lab is to practice Python **expressions and control flow** and to demonstrate understanding of:
* truthiness
* identity vs equality
* control flow (`if`, `match`, loops)
* comprehensions
* generators and lazy evaluation.

Students should show both **correct program behavior** and **understanding of Python concepts**.

## Lab Structure
```
lab02/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ answers.md
│
└─ src/
    └─ lab02.py
```

## Getting Started
Open `lab02/` and run the following to setup the environment:
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
python src/lab02.py
```

## Output Structure
The program prints six sections (A–F), each demonstrating a specific concept: truthiness, identity, equality, control flow, list comprehensions, generators, and lazy evaluation.

### Task A $-$ Truthiness
The example demostrates how Python evaluates truthiness of different objects.

### Task B $-$ Identity vs Equality
The demonstration explains how identity and equality work and the difference between them.

### Task C $-$ Control Flow
The code shows how the correct use of `if / elif` for performing simple control flows.

### Task D $-$ Pattern Matching
This task presents an example of how `match-case` can be used in Python for convenient pattern recognition.

### Task E $-$ Comprehensions
This example demonstrated the practical cases of creating lists and dictionaries by using comprehensions.

### Task F $-$ Generators
Task F uses generator structure to build a function that produces even numvers up to `limit`, and a generator expression to calculate the sum of squares of even numbers $< 1,000,000$.
# LAB03: Functions as Objects, Lambda, Closures

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--functions-as-objects)
- [Task B](#task-b--sorting-with-lambda)
- [Task C](#task-c--function-factory)
- [Task D](#task-d--closure-counter)
- [Task E](#task-e--lambda-vs-def)
- [Task F](#task-f--functional-composition)

## Goal
The goal of this lab is to explore Python functions as **first-class objects** and understand how functions can:
* be assigned to variables
* be passed as arguments
* be created dynamically
* capture variables from their environment (closures)

Students should demonstrate understanding of:
* functions as objects
* lambda expressions
* closures
* basic functional composition

## Lab Structure
```
lab03/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ answers.md
│
└─ src/
    └─ lab03.py
```

## Getting Started
Open `lab03/` and run the following to setup the environment:
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
python src/lab03.py
```

## Output Structure
The program prints six sections (A–F), each demonstrating a specific concept: Python functions, lambda expressions, closures, basic functional composition.

### Task A $-$ Functions as Objects
The example demostrates the basic use of built-in, lambda, and custom functions in Python.

### Task B $-$ Sorting with Lambda
The demonstration explains how lambda expressions can be used to sort lists by different values (e.g. age, name).

### Task C $-$ Function Factory
The code shows how to create identical functions with varying parameters through implementing a "function factory" function.

### Task D $-$ Closure Counter
This task presents an example of how closures can be used to store an internal state of a function.

### Task E $-$ Lambda vs def
This example demonstrates that both lambda expressions and def-functions behave the same way when implemented correctly.

### Task F $-$ Functional Composition
Task F uses generator and lambda expressions to perform operations on the elements of a list.
# LAB04: Higher-Order Functions, map/filter, Decorators

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--high-order-functions)
- [Task B](#task-b--map)
- [Task C](#task-c--filter)
- [Task D](#task-d--mapfilter-vs-comprehensions)
- [Task E](#task-e--simple-decorator)
- [Task F](#task-f--decorator-with-arguments)
- [Task G](#task-g--caching-decorator)

## Goal
The goal of this lab is to practice using **higher-order functions** and to understand how functions can be used to transform behavior.

Students should demonstrate understanding of:
* higher-order functions (functions as arguments and return values)
* functional transformations using map and filter
* differences between map/filter and comprehensions
* decorators and how they modify function behavior
* decorators with arguments
* basic caching techniques using decorators 

## Lab Structure
```
lab04/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ answers.md
│
└─ src/
    ├─ lab04.py
    ├─ task_a.py
    ├─ task_b.py
    ├─ task_c.py
    ├─ task_d.py
    ├─ task_e.py
    ├─ task_f.py
    └─ task_g.py
```

## Getting Started
Open `lab04/` and run the following to setup the environment:
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
python src/lab04.py
```

## Output Structure
The program prints six sections (A–F), each demonstrating a specific concept: high-order functions, map/filter, list comprehensions, decorators.

### Task A $-$ High-Order Functions
Implemented an `apply` function to demonstrate passing a function as an argument.

### Task B $-$ map
Utilized `map` to square numbers and convert numeric lists to strings.

### Task C $-$ filter
Utilized `filter` to filter lists for even numbers and values greater than 10.

### Task D $-$ map/filter vs comprehensions
Compared the implementation of data transformations using `map`/`filter` versus list comprehensions.

### Task E $-$ Simple Decorator
Created a `@call_counter` decorator that tracks and prints the number of times a function is executed.

### Task F $-$ Decorator with Arguments
Created a `@prefix(text)` decorator that takes arguments and prepends strings to function results.

### Task G $-$ Caching Decorator
Implemented a `@cache` decorator and demonstrated its performance benefits on the recursive Tribonacci sequence.
# LAB05: Type Hints, Generics, Mypy

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--basic-type-hints)
- [Task B](#task-b--typed-collections)
- [Task C](#task-c--optional)
- [Task D](#task-d--function-type)
- [Task E](#task-e--generics)
- [Task F](#task-f--functions-returning-function)
- [Task G](#task-g--pipeline)

## Goal
The goal of this lab is to practive using **type hints** and to understand how static typing improves code reliability and clarity.

Students should demonstrate understanding of:
* basic type annotations for functions
* typed collections
* generics using `TypeVar`
* function types
* static type checking with `mypy`
* strict type checking discipline (`mypy --strict`)

## Lab Structure
```
lab05/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ answers.md
│
└─ src/
    ├─ lab05.py
    │
    └─ tasks/
        ├─ task_a.py
        ├─ task_b.py
        ├─ task_c.py
        ├─ task_d.py
        ├─ task_e.py
        ├─ task_f.py
        └─ task_g.py
        │
        └─ utils/
            └─ utils.py
```

## Getting Started
Recommended Python version is `Python 3.12.6`.

Open `lab05/` and run the following to setup the environment:
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
python src/lab05.py
```
Test passing strict type checking:
```bash
mypy --strict src/lab05.py
```

## Output Structure
The program prints seven sections (A–G), each demonstrating a specific concept: typed annotations for functions, typed collections, generics, functions types.

### Task A $-$ Basic Type Hints
Implemented `add(a, b)` and `square_list` functions to demonstrate correct type annotations for functions.

### Task B $-$ Typed Collections
Utilized `filter` to leave only even numbers, demonstrated the use of typed collections.

### Task C $-$ Optional
Implemented a function that searched for an element in the list. It returns the position of the element if it is in the list, and `None` otherwise.

### Task D $-$ Function Type
Used an `apply` function to perform different operations over the variable. Showed the correct usage of function type `Callable`.

### Task E $-$ Generics
Created a `first` function that returns the first element of a list. Used `TypeVar` for correct type annotations inside the function.

### Task F $-$ Functions Returning Function
Created a `make_multiplier` function facroty to demostrate type annotations for functions that return functions.

### Task G $-$ Pipeline
Implemented a pipeline that leaves only the even elements in the list, squares them, and calculates their sum.
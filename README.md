# LAB01: Names & Objects (binding), mutability, copy, GC (CPython)

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Output Structure](#output-structure)
- [Task A](#task-a--binding-vs-rebinding)
- [Task B](#task-b--mutation-vs-rebinding)
- [Task C](#task-c--function-arguments-are-new-bindings)
- [Task D](#task-d--default-argument-trap)
- [Task E](#task-e--copy-semantics-shallow-vs-deep)
- [Task F](#task-f--reference-counting--gc-cpython)

## Goal
* Demonstrate that **n**ames are bindings to objects**, not variables in the traditional sense.
* Distinguish **rebinding vs mutation**, observe **argument passing behavior**, understand **copy semantics**, and 
explore **reference counting / garbage collection in CPython**.

This laboratory focuses on **observations and explanations**, not on writing complex code.

## Lab Structure
```
lab01
├─ README.md
├─ requirements.txt
│
├─ report
│   └─ answers.md
│
└─ src
    └─ lab01.py
```

## Getting Started
Open `lab01/` and run the following to setup the environment:
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
python src/lab01.py
```

## Output Structure
The program prints six sections (A–F), each demonstrating a specific concept: binding, mutation, argument passing, default arguments, copy semantics, and reference counting behavior.

### Task A $-$ Binding vs Rebinding
The example demostrates that names in Python are bindings, as well as rebinding mechanics.

Two names that are referring to the same object are created. Then, **rebinding** is performed. Values and ids are printed before and after the operation.

### Task B $-$ Mutation vs Rebinding
The demonstration explains how mutation works and the difference between mutation and rebinding.

Two names that are referring to the same object are created. Then, **mutation** is performed. Values and ids are printed before and after the operation.

### Task C $-$ Function arguments are new bindings
The code shows how parameters in functions work, demonstrates that the argument passing is binding, not copying.

A name is binded to an object. Two functions of mutation and rebinding are exectuted. The results are printed after each operation correspondingly.

### Task D $-$ Default argument trap
This task presents the default argument trap: in Python, default value objects are created only once and further mutated. This explains "unexpected" behavior after several funciton calls.

A function with a default argument is called twice. The states of the default argument are printed after each call.

### Task E $-$ Copy semantics (shallow vs deep)
This example demonstrated the practical difference between shallow and deep copies of nested objects.

A name `a` is created. Also, we create a shallow copy `b` and a deep copy `c`. The result of mutating `b` is shown in the output.

### Task F $-$ Reference counting / GC (CPython)
Task F uses reference counting to show an example of CPython optimization $-$ immortal objects.

Reference counting mechanics are demonstrated in the first example. It is followed by reference counting values for a usual object and two immortal ones.
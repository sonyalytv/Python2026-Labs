# LAB11: Async Batch Processor

## Table of Contents
## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Task 1](#task-1--sequential-mode-sync)
- [Task 2](#task-2--async-mode-async)
- [Task 3](#task-3--limited-mode-limited)
- [Task 4](#task-4--error-handling)
- [Task 5](#task-5--logging)

## Goal
Implement a CLI tool that processes a batch of tasks in different execution modes:
* sequential (sync) 
* concurrent (async) 
* limited concurrency (semaphore) 

The lab focuses on understanding:
* async vs sequential execution 
* await vs gather
* basic concurrency control 
* error handling strategies 

## Lab Structure
```
lab11/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ answers.md
│
└─ src/
    └─ async_tool/
        ├─ __init__.py
        ├─ __main__.py
        ├─ models.py
        └─ executor.py
```

## Getting Started
Recommended Python version is `Python 3.12.6`.

Open `lab011/` and run the following to setup the environment:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
If environment activation fails try running:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
You can run the tool as a module to see its capabilities:
```bash
python -m src.async_tool input.json --mode async --log-level INFO
```
Test passing strict type checking:
```bash
mypy --strict .
```


### Task 1 $-$ Sequential mode (`sync`)
* Processed tasks one by one.
* Utilized standard `await` inside a loop to ensure strict sequential execution.


### Task 2 $-$ Async mode (`async`)
* Configured to run all tasks concurrently.
* Utilized `asyncio.gather` to manage and await multiple coroutines simultaneously.


### Task 3 $-$ Limited mode (`limited`)
* Successfully limited the maximum number of concurrent tasks.
* Implemented an `asyncio.Semaphore` to bottleneck and control concurrent execution flow.


### Task 4 $-$ Error handling
* Implemented strict failing: Without --continue-on-error, the program stops immediately on the first failure.
* Implemented graceful degradation: With --continue-on-error, failed tasks do not crash the application, but instead produce a structured error dictionary:
```json
{
  "id": "X",
  "status": "error",
  "message": "..."
}
```


### Task 5 $-$ Logging
* Added logging to track task start and task completion times.
* Ensured the application strictly respects the user-selected log level (DEBUG, INFO, WARNING, ERROR) so output remains clean.
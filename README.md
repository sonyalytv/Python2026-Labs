# LAB12: Testing an Async CLI Tool

## Table of Contents
- [Goal](#goal)
- [Lab Structure](#lab-structure)
- [Getting Started](#getting-started)
- [Part A](#part-a--unit-tests)
- [Part B](#part-b--cli--behavior-tests)

## Goal
Write automated tests for the existing async CLI tool built in Lab 11. 

The lab focuses on understanding:
* how to test asynchronous functions
* how to test CLI applications as a user would
* the difference between unit and behavior (black-box) tests
* how to structure test files using `pytest`

## Lab Structure
```
lab12/
├─ README.md
├─ requirements.txt
│
├─ report/
│   └─ answers.md
│
├─ src/
|   ├─ __init__.py
│   └─ async_tool/
│       ├─ __init__.py
│       ├─ __main__.py
│       ├─ models.py
│       └─ executor.py
│
└─ tests/
    ├─ __init__.py
    ├─ test_process_item.py
    └─ test_cli.py
```

## Getting Started
Recommended Python version is `Python 3.12.6`.

Open `lab12/` and run the following to setup the environment:
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
To run the automated tests, use `pytest`:
```bash
# Run all tests with verbose output
pytest -v

# Run only unit tests
pytest -v tests/test_process_item.py

# Run only CLI tests
pytest -v tests/test_cli.py
```
Test passing strict type checking:
```bash
mypy --strict .
```


### Part A $-$ Unit Tests
Located in `tests/test_process_item.py`.
* Tests the individual `process_item` coroutine directly.
* Utilizes `pytest.mark.asyncio` to properly await async functions in the test environment.
* Verifies three main scenarios:
  1. **Success case:** Valid input returns the correct structure and data.
  2. **Failure case:** An item marked as `good: false` correctly raises a `ValueError`.
  3. **Basic correctness:** The returned dictionary matches the expected `TaskResult` format.


### Part B $-$ CLI / Behavior Tests
Located in `tests/test_cli.py`.
* Tests the CLI tool as a complete system from the user's perspective (Black-box testing).
* Utilizes `subprocess.run` to execute the program exactly as it would run in the terminal.
* Utilizes Pytest's `tmp_path` fixture to dynamically generate input JSON files for testing.
* Verifies:
  1. **Basic execution:** Exits with code 0 and returns valid JSON.
  2. **Mode behavior:** Functions properly when passed non-default flags (e.g., `--mode async`).
  3. **Error without flag:** Exits with a non-zero code when a task fails and no continue flag is provided.
  4. **Error with flag:** Successfully catches errors and outputs them as JSON when `--continue_on_error` is passed.
  5. **Output structure:** Ensures the correct number of items are returned and order is preserved.
# Lab 12 Report

1. What is the difference between unit tests and behavior tests?

Unit tests  verify individual components of the code (like a single function or class) to ensure the specific internal logic works correctly. Behavior tests (or black-box tests) treat the program as a complete system, interacting with it exactly as a user would (providing inputs and verifying outputs) without looking at internal implementations.

2. Why is subprocess used for CLI testing?

Using `subprocess` allows the test environment to create an entirely separate system process for the application. This ensures we are testing the true command-line interface, including argument parsing (`argparse`), environment setup, and standard output/error capture, rather than just calling a Python function inside our test suite.

3. What happens if one async task fails without error handling?

If an asynchronous task fails without being caught by a try/except block, it raises an exception. Functions like `asyncio.gather` will immediately propagate this first exception up to the caller, causing the main event loop to crash, terminating the program with a non-zero exit code, and leaving other concurrent tasks unfinished.

4. When should you test internal functions vs full system behavior?

You should test internal functions (unit tests) to verify complex algorithmic logic, edge cases, and distinct modules because these tests execute extremely fast and pinpoint the exact location of failures. You should test system behavior to verify that all the separate modules are wired together correctly and that the user receives the expected end result.

5. What are the risks of time-based tests?

Time-based tests are highly unreliable and prone to "flakiness." Execution time fluctuates wildly depending on the operating system's process scheduling, CPU load, and the hardware of the machine running the tests. A strict timing threshold that passes locally might randomly fail elsewhere.
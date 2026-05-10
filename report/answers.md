# Lab 11 Report

1. Why does `await` inside a loop lead to sequential execution?
Because `await` pauses the execution of the surrounding coroutine until the awaited task completes. Inside a loop, this prevents the loop from moving to the next iteration to start the next task, forcing them to run one at a time.

2. How does `asyncio.gather` change behavior?
It schedules multiple awaitable objects to run concurrently on the event loop. Instead of waiting for one task to finish before starting the next, it initializes all of them at once, allowing their I/O wait times to overlap.

3. What happens if one task fails in async mode without `--continue-on-error`?
When a task fails, it raises an exception. `asyncio.gather` will immediately propagate the first exception it receives up to the caller. This causes the program to stop on the first error and exit with a non-zero code.

4. Why is a semaphore needed?
A semaphore controls the number of tasks that can run at the same time. If you thousands of concurrent network or file requests are launched, we can easily hit OS limits or overload a target server. A semaphore prevents this by acting as a bottleneck.

5. When should async NOT be used?
Async should not be used for CPU-bound operations (e.g., heavy mathematical computations, image processing). Because of Python's Global Interpreter Lock (GIL), a CPU-bound task will block the entire event loop, preventing any other async tasks from running. Multiprocessing is better suited for those tasks.
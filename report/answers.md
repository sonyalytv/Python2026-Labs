# Answers to Lab01

## Table of Contents
- [Task A](#task-a--truthiness)
- [Task B](#task-b--identity-vs-equality)
- [Task D](#task-d--pattern-matching)
- [Additional Questions](#additional-questions)

## Task A $-$ Truthiness
Why does Python treat empty containers as $False$?

When the `__bool__` method is not identified, Python looks for a `__len__` method. The length of an empty container is equal to $0$, and Pythong interprets `0` as **falsy**.

## Task B $-$ Identity vs Equality
When should `is` be used instead of `==`?

In general, `is` should be used when the goal is to compare the objects themselves and not only their values. It means, we check where they are located in memory. It is especially important when comparing objects with `None`, `True` or `False`, as they are singletons. Using `==` in this case may result in an unpredicted behaviour (for instance, objects of not `NoneType` can be equal to `None`).

## Task D $-$ Pattern Matching
Why is `match` convenient for analysing structured data?

`Match` significantly simplifies pattern matching. To build the same logic using only `if-elif-else` we would have to write long expressions with `and` and `or`, but this approach is error-prone and makes the code hard to read.

## Additional Questions
1. What is the difference between a list comprehension and a generator expression?

    Generators use less memory, they do not store all the elements, they produce them one by one. In contrast, list comprehensions use $O(len(list))$ of memory.

2. Why are generators considered lazy?

    Generators are considered lazy because they produce values on the fly. They go through them one by one, and can be stopped at any moment to resume their work later.

3. What happens when a generator finishes exectution?

    A `StopIteration` exception is thrown when `__next__` method has gone through all the elements and there are no more items to produce.
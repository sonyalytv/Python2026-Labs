# Answers to Lab04

1. What is a high-order function?

    A higher-order function is a function that either takes one or more functions as arguments, returns a function as its result, or both. It treats functions as first-class objects.

2. What is the difference between `map` and list comprehension?

    * `map` is a built-in function that applies a specific transformation function to an iterable, returning a map object (an iterator)
    * list comprehension is more readable, Python-syntactic construction that generates a new list entirely, and it has the added benefit of being able to map and filter elements simultaneously in a single expression

3. What is a decorator?

    A decorator is a design pattern in Python that allows us to dynamically modify or extend the behavior of a function or method without changing its source code. It is essentially a higher-order function that wraps another function. So it adds new qualities to a function, it is useful for repeated blocks or a more unified style of functions.

4. What is the difference between a simple decorator and a decorator with arguments?

    * A simple decorator is a single wrapper function that accepts the target function as its only argument. 
    * A decorator with arguments requires an extra layer of nesting: the outerm function accepts the custom arguments and returns the actual decorator, which then accepts the target function and wraps it. So it is like a decorator factory.

5. Why is caching useful?

    * Caching stores the results of expensive or time-consuming function calls. 
    * When the function is called again with the exact same arguments, it immediately returns the stored result instead of recalculating it. 
    * This avoids unnecessary computations and improves performance, which is especially crucial for recursive algorithms.
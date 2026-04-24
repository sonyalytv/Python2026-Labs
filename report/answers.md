# Answers to Lab08

1. How does a `for` loop work with custom objects?

    It looks for `__next__` and `__iter__` methods. Firstly, it calls the `__iter__` dunder, then it repeatedly calls the `__next__` method until the `StopIteration` exception is raised, which means the end of the cycle, and prevents the program of going into an infinite loop.

2. What methods are required for iteration?

    As describes above, two methods are required for iteration: `__next__` and `__iter__`.

3. How does the `with` statement work internally?

    * Its work is similar to the `try...except...finally` block. 
    * When Python meets a `with` statement it calls `__enter__` method for the given object. If an error appear during the execution of the block, it stops the block, but the program doesn't crash. In the end,`__exit__` is called. If it returns `True` the program execution will continue after the `with` block, and will crash otherwise.

4.  When is `__exit __` called?

    * If the program runs perfectly, it is called at the end of the `with` block.
    * If we meet an early exit (`return`, `continue`, etc.), it is called immediately, and then we exit the block.
    * If an exception or an error is thrown inside the `with` block, `__exit__` method is called. It can handle the error, or not. If it returns `True` the program execution will continue after the block, and will crash otherwise.

5. What problem do descriptors solve?

    Descriptors help to write reusable code. It is a class that defines setter/getter logic, and then it can be attributed to any variable that needs to follow these rules. This way, we implement this logic only once, and can reuse anywhere we need it.

6. What happens if a descriptor is not used?

    We need to solve the stated above problem in a different way.
    * Use the usual `__init__` method, but no data validation will be performed when binding to a new value. So the program can crash unexpectedly during execution.
    * Define setters and getters for each object separately. The code will have the same behavior. But the code gets difficult to support and develop. In case, if the validation rule changes, we will have to change it in each object. Also, the amount of code is bigger if we use this approach.

7. Why is direct iteration preferred over index-based loops in Python?

    * The code is much more readable if we use direct iteration.
    * Not all data types have indexes (e.g., sets or dictionaries). Direct iteration is more flexible and can handle seamlessly more data types. The only requirement is that the object is iterable.
    * When using iterators and not indexes, we are less likely to get an `index-out-of-range` error if the implementation is correct.
    * It is a bit faster, as we don't need to calculate the index, and call a __getitem__ method to get the next value.
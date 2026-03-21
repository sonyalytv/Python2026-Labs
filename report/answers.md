# Answers to Lab03

1. What does it mean that functions in Python are **first-class objects**?

    It means that functions are objects in memory, and we can use them as any other object. We can assign them to variables, store them in containers, pass them as arguments to other functions, and return them from functions.

2. What is the difference between a function defined with `def` and a `lambda` expression?

    * Def-functions have a name, lambda-functions are anonymous (their name is $lambda$).
    * Def-functions can be complex, have multiple expressions and statements. Lambdas can only have a single expression.
    * Lambdas always return a value. Usual don't have to return a value, if it is needed they use `return` keyword.
    * Mostly, the code is more readable when using def-functions.
    * We use lambda expressions for short, simple, non-reusable functions.

3. What is a **closure**?

    It is a nested function that allows us to access variables of the outer function even when the outer funcion is closed.

4. In what situtations are closures useful?

    Most commonly, closures are used to create function factories, callbacks, data encapsulation, and decorators.
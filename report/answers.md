# Answers to Lab05

1. What is the purpose of type hints in Python?

    * Type hints make it easier to catch errors in advance, during development. Some type checkers like `mypy` can analyze your code before actually running it. It notices type-related errors, like calling a method that doesn't exist for strings. This way the program is less likely to crash unexpectedly in production.
    * Type hints make the code much easier to read. They provide clear instructions of what to pass in and what we will get back.
    * Additionally, some IDEs can give better autocomplete suggestions and underline potential errors while writing code if type hints are given.

2. What is the difference between `Any` and a generic type `T`?

    * `Any` means that we do not care of which type the variable will be. It is like we are 'turning off' the type check.
    * `T` is more strict. When the variable is passed to the function it binds to this exact type, and checks it throughout the function's execution. It is often used when writing generalized functions or classes that work with various types. For instance, it is used when we need to return the same type that we passed in.
    * The main difference is that generic types provide some level of safety, while `Any` literally means ingnoring the variable type.

3. What does `Callable[[int], int] describe?

    It describes a type of an object that can be passed to a function or a class, for example. It means a function or any other object that can be called that receives one `int` variable as input and outputs an `int` value as well. So it can be any kind of a unary operation with integer numbers.

4. Why does `mypy --strict` require more annotations?

    By default, `mypy` allows to mix typed code with completely untyped code. If a function doesn't have annotations, `mypy` assumes that it returns the `Any` type. When using the `--strict` flag, we have to explicitly declare types everywhere. When this assuming doesn't work, we need to writh only fully typed functions, all containers (like `list` or `dict`) must have a specified type of what is inside them. In general, `mype --strict` ensures that the compiler knows the exact type of our data at every step.
# Answers to Lab06

1. What is stored in `obj.__dict__`?

    It is a dictionary that stores an object's attributes. Keys are attributes names, and values are the corresponding values of these attributes.

2. What is the difference between a class and an object?

    * A class is like a template to create objects, it is similar to a data type. While objects are specific instances that contain data.
    * One class can have many objects that are instances of this class.

3. What does `__init__` do?

    It is a dunder that is called automatically when an object is created. It initializes the object's attributes values.

4. Who calls `__str__`, and when?

    It is called by `print()` and `str()` functions to produce a readable, user-friendly string representation of the object.

5. What is the difference between `==` and `is`?

    `==` checks the equality of the object values, while `is` checks the identity and is only `True` when the names refer to the same address in memory.

6. Why do we use `other: object` in `__eq__` and `__lt__`?

    To follow the `mypy --strict` typing rules. We should be able to call these methods with any other object. This way we can accept a general `object` without typing issues and then check the type using `isinstance` before comparing.
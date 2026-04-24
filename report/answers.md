# Answers to Lab07

1. What is duck typing?

    It is the principle of typing in Python, JavaScript, and some other programming languages: "If it walks like a duck and it quacks like a duck, then it must be a duck."
    * It gives more flexibility than strict typing. The code can be more generic and work with different types of objects without the need to implement complex inheritance flows or interfaces.
    * Thus, the code gets shorter and it takes less time to write it.
    * However, it can lead to runtime errors and program crashes because the type isn't checked before the program runs.

2. How does Protocol differ from ABC?

    * ABC requires inheritance, while Protocol doesn't.
    * When using ABC, classes are tied to it. With Protocol, classes don't even need to know that the Protocol exists.
    * In general, Protocol is more flexible, and is used for reusable functions that accept any object, as long as it behaves the right way.
    * ABC is used for building a strict framework, where classes share code and must belong together, which is stated clearly by inheritance.

3. Does Protocol require inheritance? Why or why not?

    No, Protocol doesn't require inheritance. It works this way because its purpose is to simplify the code. It allows type checkers to verify that objects can perform certain actions without forcing those object into a strict set of specific data types.

4.  What problem does ABC solve?

    * It requires classes to have the needed methods. This way, the object creation fails if doesn't follow the pattern. It makes error tracking much easier in large projects. 
    * Also, it is used for the Template Method Pattern. So sublclasses can have some helper methods and the developer doesn't have to rewrite all the code for each subclass.

5. What does `@dataclass` generate automatically?

    * `__init__` $-$ the constructor. It takes all the fields defined and assigns them to `self`.
    * `__repr__` $-$ the string representation.
    * `__eq__` $-$ the equality checker. It allows to compare two object using `==`. It returns `True` if both objects are of the same class and their fields contain the same values.

6. What changes when using `slots`?

    The object doesn't act as a dynamic dictionary any more. It is impossible to add fields if they aren't explicitly defined in the class. It helps to prevent passing values to misspelled fields. So the object gets stricter, and more memory efficient.

7. Why does Protocol work with different implementations (regular class, dataclass, slots)?

    * Protocol looks at the public "surface" of an object, and doesn't care about its inside structure. It only checks that the required methods exist.
    * Protocol ensures the expected behavior of objects, and doesn't restrict their state in any way.
import math

def TaskA():
    print("========================================")
    print("===   Task A: Functions as Objects   ===")
    print("========================================")

    def apply_twice(func, x):
        return func(func(x))
    
    def sqr_custom(x):
        return x ** 2
    
    print("Applying the following functions twice to x = 3:")
    print("lambda x: x + 3  ->  ", apply_twice(lambda x: x + 3, 3))
    print("math.sqrt        ->  ", apply_twice(math.sqrt, 3))
    print("sqr_custom       ->  ", apply_twice(sqr_custom, 3), "\n")


def TaskB():
    print("========================================")
    print("====   Task B: Sorting with Lambda   ===")
    print("========================================")

    people = [
        ("Alice", 25),
        ("Bob", 20), 
        ("Carol", 30),
        ("Dave", 22)
    ]

    print("Sorted by age:")
    print(sorted(people, key = lambda p: p[1]), '\n')
    print("Sorted by name:")
    print(sorted(people, key = lambda p: p[0]), '\n')


def TaskC():
    print("========================================")
    print("=====   Task C: Function Factory   =====")
    print("========================================")

    def make_multiplier(k):
        def multiply(x):
            return x * k
        return multiply
    
    print("Multiply 10 x 3 = 30")
    times3 = make_multiplier(3)  # by what we multiply
    print(times3(10))  # what we multiply

    print("Multiply 5 x 7 = 35")
    times7 = make_multiplier(7)
    print(times7(5), '\n')


def TaskD():
    print("========================================")
    print("======   Task D: Closure Counter   =====")
    print("========================================")

    def counter():
        n = 0
        def inc():
            nonlocal n
            n += 1
            return n
        return inc
    
    c = counter()
    print("c = counter()")
    print(f"c() -> {c()}")
    print(f"c() -> {c()}")
    print(f"c() -> {c()}\n")


def TaskE():
    print("========================================")
    print("=======   Task E: Lambda vs def   ======")
    print("========================================")

    def sqr(x):
        return x * x
    
    sqr_custom = sqr
    sqr_lambda = lambda x: x * x
    x = 5
    print("Perform x^2, x = 5 using def- and lambda-functions:")  # they act the same way
    print(sqr_custom(x), "<=>", sqr_lambda(x), '\n')


def TaskF():
    print("========================================")
    print("==   Task F: Functional Composition   ==")
    print("========================================")

    numbers = list(range(1, 9))
    sum_lambda = sum(map(lambda x: x * x * (1 - x % 2), numbers))
    sum_generator = sum(x * x for x in numbers if x % 2 == 0)

    print("Lambda and generator expession give the same results")
    print(sum_lambda, "==", sum_generator, "\n")


TaskA()
TaskB()
TaskC()
TaskD()
TaskE()
TaskF()
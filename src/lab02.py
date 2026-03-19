import sys

def TaskA():
    print("========================================")
    print("========   Task A: Truthiness   ========")
    print("========================================")

    print("Checking truthiness of the following values:")
    print(f"value: 0 -> {bool(0)}")
    print(f"value: 1 -> {bool(1)}")
    print(f"value: 0.0 -> {bool(0.0)}")
    print(f"value: 0.33 -> {bool(0.33)}")
    print(f"value: [] -> {bool([])}")
    print(f"value: [1, 2, 3] -> {bool([1, 2, 3])}")
    print(f"value: {{}} -> {bool({})}")
    print(f"value: {{'Hello': 'World!'}} -> {bool({'Hello': 'World!'})}")
    print(f"value: \"\" -> {bool("")}")
    print(f"value: \"Lab02\" -> {bool("Lab02")}")
    print(f"value: None -> {bool(None)}\n")


def TaskB():
    print("========================================")
    print("===   Task B: Identity vs Equality   ===")
    print("========================================")

    # create two separate objects with the same values
    a = [1, 2, 3]
    b = [1, 2, 3]
    print("Case #1: equal values but different objects")
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    print(f"a == b -> {a == b}")
    print(f"a is b -> {a is b}\n")

    b = a
    print("Case #2: identical objects")
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    print(f"a == b -> {a == b}")
    print(f"a is b -> {a is b}\n")

    a = "Hello"
    b = "Hello"
    print("Case #3: immutable objects")
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    print(f"a == b -> {a == b}     <- use this to compare")
    print(f"a is b -> {a is b}     <- unpredicted behaviour!\n")

    a = 42
    b = 42
    print("Case #4: immortal objects")
    print(f"a = {a}, id(a) = {id(a)}")
    print(f"b = {b}, id(b) = {id(b)}")
    print(f"a == b -> {a == b}     <- use this for usual comparison")
    print(f"a is b -> {a is b}     <- be careful - always True for immortal\n")


def TaskC():
    print("========================================")
    print("=======   Task C: Control Flow   =======")
    print("========================================")

    def describe_number(x):
        if x < 0:
            return "negative"
        elif x == 0:
            return "zero"
        elif x < 10:
            return "small positive"
        else:
            return "large positive"
        
    print("Calling describe_number function for different values of x:")
    x = -5
    print(f"x = {x} -> {describe_number(x)}")
    x = 0
    print(f"x = {x} -> {describe_number(x)}")
    x = 1
    print(f"x = {x} -> {describe_number(x)}")
    x = 9
    print(f"x = {x} -> {describe_number(x)}")
    x = 10
    print(f"x = {x} -> {describe_number(x)}")
    x = 100500
    print(f"x = {x} -> {describe_number(x)}\n")

def TaskD():
    print("========================================")
    print("=====   Task D: Pattern Matching   =====")
    print("========================================")

    def print_event(event):
        match event:
            case ("click", x, y):
                print(f"click at {x} {y}\n")
            case ("keypress", key):
                print(f"key pressed: {key}\n")
            case ("quit", ):
                print("quit event\n")
            case _:    # wildcard
                print("Error: uknown event type\n")

    e1 = ("click", 13, 76)
    e2 = ("keypress", "B")
    e3 = ("quit",)
    e4 = ("input", "hello")
    print(f"Event description: {e1}")
    print_event(e1)
    print(f"Event description: {e2}")
    print_event(e2)
    print(f"Event description: {e3}")
    print_event(e3)
    print(f"Event description: {e4}")
    print_event(e4)


def TaskE():
    print("========================================")
    print("======   Task E: Comprehensions   ======")
    print("========================================")

    a = [i*i for i in range (1, 21)]
    b = [x for x in a if x % 2 == 0]
    c = {x: x*x for x in range(1, 11)}
    print(a, b, c, sep = '\n', end = '\n\n')


def TaskF():
    print("========================================")
    print("========   Task F: Generators   ========")
    print("========================================")

    # generate even numbers up to limit
    def even_numbers(limit):
        for i in range(0, limit+1, 2):
            yield i

    print("Even numbers up to 15:")
    g1 = even_numbers(15)
    for i in g1:
        print(i)

    # calculate sum of squares of even numbers < 1,000,000
    g2 = (i*i for i in range(1000000) if i % 2 == 0)   # a generator not a list
    sum = 0
    for i in g2:
        sum += i
    print(f"Sum of squares of even numbers < 1,000,000 = {sum}\n")


TaskA()
TaskB()
TaskC()
TaskD()
TaskE()
TaskF()
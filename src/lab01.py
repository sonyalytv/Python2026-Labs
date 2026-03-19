import copy
import sys

def TaskA():
    print("========================================")
    print("===   Task A: Binding vs Rebinding   ===")
    print("========================================")

    # Creating two names bound to the same object
    a = 3
    b = a
    print("Initial state:")
    print(f"a = {a}, b = {b}")
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}\n")

    # Rebind a
    a = 4
    print("After rebinding a = 4:")
    print(f"a = {a}, b = {b}")
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}\n")


def TaskB():
    print("========================================")
    print("===   Task B: Mutation vs Rebinding   ==")
    print("========================================")

    # Creating two names bound to the same object
    a = [1, 2]
    b = a
    print("Initial state:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}\n")

    # Mutating the object
    b.append("Mutation")
    print("After mutation:")
    print(f"a = {a}")
    print(f"b = {b}\n")
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}\n")


def TaskC():
    print("========================================")
    print("====   Task C: Function arguments   ====")
    print("========================================")

    def mutate_list(a):
        a.append(1)

    def rebind_list(a):
        a = [1, 2]

    a = []
    print("Before call:")
    print(f"a = {a}\n")

    mutate_list(a)
    print("After mutate_list(a):")
    print(f"a = {a}\n")

    rebind_list(a) # 'a' didn't change to [1, 2]
    print("After rebind_list(a):")
    print(f"a = {a}\n")


def TaskD():
    print("========================================")
    print("===   Task D: Default argument trap   ==")
    print("========================================")

    def f(x = []):
        x.append(1)
        return x
    
    print("First call:")
    print(f(), "\n")

    print("Second call:")
    print(f(), "\n")


def TaskE():
    print("========================================")
    print("======   Task E: Copy semantincs   =====")
    print("========================================")

    a = [[1, 2]]
    b = a.copy()
    c = copy.deepcopy(a)

    print("Initial state:")
    print(f"a = {a}\n")

    b[0].append(3)
    print("After modifying b:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}\n")


def TaskF():
    print("========================================")
    print("====   Task F: Reference counting   ====")
    print("========================================")

    x = []
    print(f"Created an object and a reference: {sys.getrefcount(x)}")
    y = x
    print(f"Created one more binding: {sys.getrefcount(x)}\n")

    print(f"Refcount(42) = {sys.getrefcount(42)}")
    print(f"Refcount(1234) = {sys.getrefcount(1234)}")
    print(f"Refcount(None) = {sys.getrefcount(None)}")


TaskA()
TaskB()
TaskC()
TaskD()
TaskE()
TaskF()
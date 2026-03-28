def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{text}: {result}"
        return wrapper
    return decorator

@prefix("INFO")
def get_data():
    return "data"

def task_f() -> None:
    print("========================================")
    print("=   Task F: Decorator with Arguments   =")
    print("========================================")

    print("@prefix(\"INFO\")")
    print("def get_data():")
    print("    return \"data\"")
    print()
    print("Result:")
    print(get_data())
    print()
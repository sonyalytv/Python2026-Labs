def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"call #{wrapper.calls}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@call_counter
def say_hello():
    print("Hello!")

def task_e() -> None:
    print("========================================")
    print("===     Task E: Simple Decorator     ===")
    print("========================================")

    say_hello()
    say_hello()
    say_hello()
    print()

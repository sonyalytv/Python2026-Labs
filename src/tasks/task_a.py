from utils.utils import add_task_header

def add(a: int | float, b: int | float) -> int | float:
    return a + b

def square_list(data: list[int | float]) -> list[int | float]:
    return [x * x for x in data]

@add_task_header("A", "Basic Type Hints")
def task_a() -> None:
    print(f"add(3, 5) -> {add(3, 5)}")
    print(f"add(3.5, 7) -> {add(3.5, 7)}")
    print(f"add(3.5, 7.7) -> {add(3.5, 7.7)}")
    print(f"square_list([1, 2, 3]) -> {square_list([1, 2, 3])}")
    print(f"square_list([1.5, 2.1, 3.6]) -> {square_list([1.5, 2.1, 3.6])}")
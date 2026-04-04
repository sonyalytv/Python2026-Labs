from utils.utils import add_task_header
from typing import Callable

def square(x: int) -> int:
    return x * x

def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

@add_task_header("D", "Function Type")
def task_d() -> None:
    # check with a normal function
    print(f"apply(square, 5) -> {apply(square, 5)}")
    # check with a lambda-function
    print(f"apply(lambda x: x * 3 - 42, 7) -> {apply(lambda x: x * 3 - 42, 7)}")
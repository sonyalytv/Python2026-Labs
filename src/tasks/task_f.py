from utils.utils import add_task_header
from typing import Callable

def make_multiplier(k: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * k
    return multiplier

@add_task_header("F", "Function Returning Function")
def task_f() -> None:
    mult_3 = make_multiplier(3)
    mult_5 = make_multiplier(5)

    print(f"mult_3(7) -> {mult_3(7)}")
    print(f"mult_5(-6) -> {mult_5(-6)}")
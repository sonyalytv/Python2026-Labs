from utils.utils import add_task_header
from typing import Callable, Iterator

def custom_filter(items: list[int], func: Callable[[int], bool]) -> list[int]:
    results = []
    for item in items:
        if func(item):
            results.append(item)
    return results

def square(items: list[int]) -> Iterator[int]:
    return (x * x for x in items)

def calc_sum(items: Iterator[int]) -> int:
    result = 0
    for item in items:
        result += item
    return result


@add_task_header("G", "Pipeline")
def task_g() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Original data: {numbers}")
    print(f"2*2 + 4*4 + 6*6 + 8*8 = {calc_sum(square(custom_filter(numbers, lambda x: x % 2 == 0)))}")
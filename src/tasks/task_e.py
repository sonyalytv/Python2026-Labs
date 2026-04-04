from utils.utils import add_task_header
from typing import TypeVar, Sequence

T = TypeVar('T')

def first(items: Sequence[T]) -> T | None:
    if len(items) == 0:
        return None
    return items[0]

@add_task_header("E", "Generics")
def task_e() -> None:
    data = [1, 2, 3, 4, 5]
    print(f"list={data} -> list[0]={first(data)}")

    data1 = ["three", "five", "eight"]
    print(f"list={data1} -> list[0]={first(data1)}")

    data2 = ["hi", 3, 5, False]
    print(f"list={data2} -> list[0]={first(data2)}")

    data3 = [True, "two", 1]
    print(f"list={data3} -> list[0]={first(data3)}")
from utils.utils import add_task_header

# Returns the position of an element if found, and None otherwise
def find(data: list[int], x: int) -> int | None:
    for i, d in enumerate(data):
        if d == x:
            return i
    return None

@add_task_header("C", "Optional")
def task_c() -> None:
    data = [5, 6, 2, 11, 3, 17, 6]
    
    print(f"Original data: {data}")
    print(f"find(4): {find(data, 4)}")
    print(f"find(11): {find(data, 11)}")
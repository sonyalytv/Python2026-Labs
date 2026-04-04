from utils.utils import add_task_header

def filter_even(data: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, data))

@add_task_header("B", "Typed Collections")
def task_b() -> None:
    data = [3, 5, 2, 7, 4, 6]
    filtered_data = filter_even(data)
    
    print(f"Original data: {data}")
    print(f"After filter_even: {filtered_data}")
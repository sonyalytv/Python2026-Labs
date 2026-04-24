from typing import Callable, Any

def add_task_header(letter: str, name: str) -> Callable[[Any], Any]:
    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            full_name = f"Task {letter}: {name}"
            print("=" * 50)
            cnt = 50 - len(full_name) - 6
            print(f"{"=" * ((cnt + 1) // 2)}   {full_name}   {"=" * (cnt // 2)}")
            print("=" * 50)

            result = func(*args, **kwargs)
            print()
            
            return result
        return wrapper
    return decorator
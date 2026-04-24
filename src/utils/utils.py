from typing import Callable, Any, Self

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

class ValidGrade:
    def __init__(self, n: float = 0.0) -> None:
        self._value = n

    def __get__(self, instance: Any, owner: Any) -> Any:
        return instance._value

    def __set__(self, instance: Any, value: Any) -> None:
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100")
        instance._value = value

class Student:
    name: str
    group: str
    grade = ValidGrade()

    def __init__(self, name: str, group: str, grade: float) -> None:
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"Student -> name: {self.name}, group: {self.group}, grade: {self.grade}"
    
class StudentCollection:
    def __init__(self, students: list[Student]) -> None:
        self.students = students
        self.n = len(students)

    def __iter__(self) -> Self:
        self.curr = 0
        return self
    
    def __next__(self) -> Student:
        if self.curr >= self.n:
            raise StopIteration
        id = self.curr
        self.curr += 1
        return self.students[id]
    
    def __enter__(self) -> Self:
        print("Enter StudentCollection context")
        return self
    
    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> bool:
        print("Exit StudentCollection context")
        return True
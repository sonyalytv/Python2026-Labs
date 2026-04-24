from utils import add_task_header, export
from dataclasses import dataclass

@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"StudentData: name = {self.name}, group = {self.group}, average_grade = {self.average_grade}"

@add_task_header("B", "Dataclass implementation")
def task_b() -> None:
    student = StudentData("Vova", "MIT-424", 82.1)
    print("Created an object 'student' of StudentData class")
    print(student.serialize())
    print("Called export(student):")
    export(student)
    print()
    
    print(f"This object has __dict__:")
    print(student.__dict__)
    print()
    print(f"And doesn't have __slots__:")
    try:
        print(student.__slots__)
    except AttributeError:
        print(f"Tried to access __slots___, but caught an AttributeError")

if __name__ == "__main__":
    task_b()
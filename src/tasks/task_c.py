from utils import add_task_header, export
from dataclasses import dataclass

@dataclass(slots=True)
class StudentSlots:
    name: str
    group: str
    average_grade: float
    # __slots__ = ("name", "group", "average_grade")

    def serialize(self) -> str:
        return f"StudentSlots: name = {self.name}, group = {self.group}, average_grade = {self.average_grade}"

@add_task_header("C", "Slots")
def task_c() -> None:
    student = StudentSlots("Maria", "E-521", 98.3)
    print("Created an object 'student' of StudentSlots class")
    print(student.serialize())
    print("Called export(student):")
    export(student)
    print()

    try:
        student.first_name = "Korobka"
    except AttributeError:
        print("Tried to add a new attribute 'first_name', but caught an AttributeError")
    print()

    print(f"This object has __slots__:")
    print(student.__slots__)
    print()
    print(f"And doesn't have __dict__:")
    try:
        print(student.__dict__)
    except AttributeError:
        print(f"Tried to access __dict___, but caught an AttributeError")

if __name__ == "__main__":
    task_c()
from utils import add_task_header, export
from abc import ABC, abstractmethod

class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade
    
    def serialize(self) -> str:
        return f"StudentABC: name = {self.name}, group = {self.group}, average_grade = {self.average_grade}"

def print_obj(obj: SerializableABC) -> None:
    print(obj.serialize())

@add_task_header("D", "ABC version")
def task_d() -> None:
    student = StudentABC("Daryna", "XT-1323", 91.7)
    print("Created an object 'student' of StudentABC class")
    print(student.serialize())
    print("Protocol -> Called export(student):")
    export(student)
    print("ABC interface -> Called print_obj(student):")
    print_obj(student)

if __name__ == "__main__":
    task_d()
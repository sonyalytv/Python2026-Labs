from utils import add_task_header, export

class StudentRegular:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"StudentRegular: name = {self.name}, group = {self.group}, average_grade = {self.average_grade}"

@add_task_header("A", "Regular class (duck typing)")
def task_a() -> None:
    student = StudentRegular("Mykola", "KN-123", 90.7)
    print("Created an object 'student' of StudentRegular class")
    print(student.serialize())
    print("Called export(student):")
    export(student)

if __name__ == "__main__":
    task_a()
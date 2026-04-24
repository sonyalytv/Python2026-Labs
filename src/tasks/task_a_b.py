from utils import add_task_header, Student, StudentCollection

@add_task_header("A", "Iteration")
def task_a() -> None:
    collection = StudentCollection([
        Student("Tetyana", "KN-125", 88.8),
        Student("Mykola", "XT-1122", 99.9),
        Student("Yegor", "E-1621", 86.3),
    ])

    for student in collection:
        print(student)

@add_task_header("B", "Context Manager")
def task_b() -> None:
    students = [
        Student("Tetyana", "KN-125", 88.8),
        Student("Mykola", "XT-1122", 99.9),
        Student("Yegor", "E-1621", 86.3),
    ]

    with StudentCollection(students) as collection:
        print("the 'with' block body")
        raise OSError
        # will not be printed, __exit__ is called
        print("After error")

    print("After the 'with' block we can continue execution")

if __name__ == "__main__":
    task_a()
    task_b()
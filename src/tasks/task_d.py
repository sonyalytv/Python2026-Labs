from utils import add_task_header, Student, StudentCollection

@add_task_header("D", "Integration")
def task_d() -> None:
    students = [
        Student("Tetyana", "KN-125", 88.8),
        Student("Mykola", "XT-1122", 99.9),
        Student("Yegor", "E-1621", 77.77),
    ]
    with StudentCollection(students) as collection:
        for student in collection:
            print(student.grade)
    print()
    print("Demonstrated that all the created components can be used together")

if __name__ == "__main__":
    task_d()
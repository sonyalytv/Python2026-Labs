from utils import add_task_header, Student

@add_task_header("C", "Descriptor")
def task_c() -> None:
    student = Student("Ksenia", "MIT-1123", 42.42)
    print("Created a student object:")
    print(student)
    try:
        new_grade = 90.99
        student.grade = new_grade
        print(f"Successfully changed the grade: {student.grade}")
    except ValueError as e:
        print(f"Tried to change the grade to {new_grade}, but caught a ValueError: {e}")

    try:
        new_grade = 125.14
        student.grade = new_grade
        print(f"Successfully changed the grade: {student.grade}")
    except ValueError as e:
        print(f"Tried to change the grade to {new_grade}, but caught a ValueError: {e}")


if __name__ == "__main__":
    task_c()
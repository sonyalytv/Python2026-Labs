from student import Student
from utils import print_header

# Task A
print_header("A", "Define the 'Student' class")
s1 = Student("Petro", "KN-124", 97.3)
s2 = Student("Maria", "KN-125", 76.8)
print("Student 1 attributes:")
print(f"Name: {s1.name}")
print(f"Group: {s1.group}")
print(f"Grade: {s1.average_grade}")
print("Student 2 attributes:")
print(f"Name: {s2.name}")
print(f"Group: {s2.group}")
print(f"Grade: {s2.average_grade}")
print()

# Task B
print_header("B", "Inspect internal structure")
print(f"Initial student 1 __dict__: {s1.__dict__}")
s1.__dict__["group"] = "KN-124a"
print(f"Modified 'group' via __dict__: {s1.__dict__}")
print()

# Task C
print_header("C", "Implement '__str__'")
print("Student info:")
print(s1)
print(s2)
print()

# Task D
print_header("D", "Implement '__repr__'")
print("Formal student info:")
print(repr(s1))
print(repr(s2))
print()

# Task E
print_header("E", "Implement equality ('__eq__')")
s3 = Student("Petro", "KN-124a", 97.3)
print(f"s1 = {repr(s1)}, id(s1) = {id(s1)}")
print(f"s2 = {repr(s2)}, id(s2) = {id(s2)}")
print(f"s3 = {repr(s3)}, id(s3) = {id(s3)}")
print(f"s1 == s2: {s1 == s2}")
print(f"s1 == s3: {s1 == s3}")
print()

# Task F
print_header("F", "Implement ordering ('__lt__')")
print(f"Student 1: {s1}")
print(f"Student 2: {s2}")
print(f"s1 < s2: {s1 < s2}")
s5 = "Unknown Student"
print("s1 < 'Unknown Student' -> ", end="")
try:
    print(s1 < s5)
except TypeError as e:
    print(f"Caught error: {e}")
print()

# Task G
print_header("G", "Sorting")
students = [
    Student("Andriy", "KN-124", 98.2),
    Student("Polina", "MIT-123", 76.5),
    Student("Ostap", "E-122", 84.6),
]
print("Before sorting:")
for s in students:
    print(s)
print()

students.sort()

print("After sorting by average_grade:")
for s in students:
    print(s)
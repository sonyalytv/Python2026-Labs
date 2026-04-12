class Student:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def __str__(self) -> str:
        return f"Student: {self.name} (group={self.group}, grade={self.average_grade})"

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', group='{self.group}', average_grade={self.average_grade})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        
        return other.name == self.name and other.group == self.group and other.average_grade == self.average_grade
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            raise TypeError(f"Comparison is not supported between objects 'Student' and '{type(other)}'")
        
        return self.average_grade < other.average_grade
        
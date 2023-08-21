"""
Ассоциация
"""

class Proffessor:
    def __init__(self, name) -> None:
        self.name = name
        

class Student:
    def __init__(self, name) -> None:
        self.name = name
        

class Course:
    def __init__(self, name, professor, students) -> None:
        self.name = name
        self.professor = professor
        self.student = students


pr1 = Proffessor('Doctor Ivalov')
st1 = Student('Vasylii')
st2 = Student('Aleksandr')

course = Course('Hight mathematic 1', pr1, [st1, st2])
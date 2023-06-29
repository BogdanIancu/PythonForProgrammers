import csv
import sys
from pathlib import Path
import greet as s
import hello as h
import mathematics.operations as m
import mathematics.basic_operations.basic_operations as b

csv.reader("test.csv")
print(dir(csv))
# print(dir(pathlib))
print(dir(Path))
print(sys.path)
s.greet("Earth")
h.greet()
print(m.do_sum(3, 5))
print(b.increment(2))


# class related stuff starts here
class Student:
    # __slots__ = "__social_number", "_specialization", "name", "age", "grade"
    id = 0
    university = "Oxford"

    def __init__(self, name="", age=0, grade=1.0):
        self.__social_number = 0
        self._specialization = "Unknown"
        self.name = name
        self.age = age
        self.grade = grade

    def __del__(self):
        print("Destructor called")

    def __add__(self, other):
        return self.grade + other.grade

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"Student (name={self.name}, age={self.age}, grade={self.grade})"

    def print_student(self):
        print(self.name, self.age, self.grade)

    @property
    def social_number(self):
        return self.__social_number + 100

    @social_number.setter
    def social_number(self, social_number):
        if social_number > 0:
            self.__social_number = social_number

    @staticmethod
    def print_university():
        print(Student.university)

    @classmethod
    def create_named_student(cls, name):
        student = cls(name)
        return student


class University:
    pass


student1 = Student("John", 20, 8.7)
print(student1.name)
print(Student.id)
student1.id = 99
student1.university = "Harvard"
print(student1.university)
print(Student.id)
print(student1.id)
Student.id = 5
student2 = Student("Mary", 19, 9.3)
print(student2.id)
student2.id = 55
print(student2.id)
print(student2._specialization)
print(isinstance(student1, Student))
student2.print_student()
del student1
Student.print_university()

uni1 = University()
uni1.name = "MIT"
print(uni1.name)

student3 = Student.create_named_student("George")
student3.print_student()
student3.social_number = 123
print(student3.social_number)
print(student2 + student3)
print(student2 == student3)
print(student3)

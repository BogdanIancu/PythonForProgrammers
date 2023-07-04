from abc import ABC, abstractmethod
import functools
import datetime


class InvalidAgeError(Exception):
    pass


def logger(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Function {function.__name__} called at {datetime.datetime.now()}")
        return function(*args, **kwargs)
    return wrapper


class BaseClass(ABC):
    @abstractmethod
    def method(self):
        pass


class Student(BaseClass):
    university = "Oxford"

    def __init__(self, name="", age=0, grade=1.0):
        self.__social_number = 0
        self._specialization = "Unknown"
        self.name = name
        if age < 0:
            raise InvalidAgeError()
        else:
            self.age = age
        self.grade = grade

    def __add__(self, other):
        return self.grade + other.grade

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"Student (name={self.name}, age={self.age}, grade={self.grade})"

    def __hash__(self):
        return (self.name.__hash__() * 31 ** 2) * 31 * self.age * int(self.grade * 100)

    def method(self):
        print("I am a student")

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


class Employable:
    def __init__(self, name):
        self.name = name


class GraduateStudent(Employable, Student):
    def __init__(self, name, graduation_year):
        Student.__init__(self, name)
        # super().__init__(name)
        Employable.__init__(self, name)
        self.graduation_year = graduation_year

    @logger
    def method(self):
        print("I am a graduate student")


def say_hello(name, salutation=""):
    print(f"Hello, {salutation} {name}!")


class Duck:
    def method(self):
        print("I am a duck")


class MyIterableType:
    __names = ["Ana", "Bob", "Chris", "Demeter"]
    __current_index = -1

    def __iter__(self):
        self.__current_index = -1
        return self

    def __next__(self):
        if self.__current_index < len(self.__names) - 1:
            self.__current_index += 1
            return self.__names[self.__current_index]
        else:
            raise StopIteration()


student1 = Student("John", 23, 9.3)
print(isinstance(student1, object))
graduate_student1 = GraduateStudent("Maria", 2023)
print(graduate_student1.__dict__)
print(issubclass(GraduateStudent, Student))
say_hello("Mark")
say_hello("Mark", "Mr")
student1.method()
print("->", graduate_student1.method.__name__)
graduate_student1.method()
student2 = Student("George", 21, 9.8)

print()
duck = Duck()
my_list = [student1, graduate_student1, student2, duck]
[s.method() for s in my_list if isinstance(s, BaseClass)]
iterable_type = MyIterableType()

counter = 0
for i in iterable_type:
    if counter == 1:
        break
    print(i)
    counter += 1

for i in iterable_type:
    print(i)


def func1(msg):
    def func2():
        nonlocal msg
        msg = msg * 2
        print(msg)
    return func2


hi_function = func1("Hi")
bye_function = func1("Bye")
hi_function()
bye_function()
hi_function = "some other value"

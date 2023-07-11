import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

BaseClass = declarative_base()

student_discipline_association = sqlalchemy.Table(
    'student_discipline',
    BaseClass.metadata,
    sqlalchemy.Column('student_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('students.id')),
    sqlalchemy.Column('discipline_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('disciplines.id'))
)


class University(BaseClass):
    __tablename__ = "universities"
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column("name", sqlalchemy.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.id} {self.name}"


class Student(BaseClass):
    __tablename__ = "students"
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column("name", sqlalchemy.String)
    age = sqlalchemy.Column("age", sqlalchemy.Integer)
    grade = sqlalchemy.Column("grade", sqlalchemy.Float)
    university = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("universities.id"))
    disciplines = relationship('Discipline', secondary=student_discipline_association, back_populates='students')

    def __init__(self, name, age, grade, university_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.university = university_id

    def __repr__(self):
        return f"Student({self.id} {self.name} {self.age} {self.grade})"


class Discipline(BaseClass):
    __tablename__ = 'disciplines'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    students = relationship('Student', secondary=student_discipline_association, back_populates='disciplines')


engine = sqlalchemy.create_engine("sqlite:///my_database.db", echo=True)
BaseClass.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

university = University("Harvard")
# session.add(university)
# session.commit()

student1 = Student("John", 21, 9.3, university.id)
student2 = Student("Maria", 23, 9.8, university.id)
student3 = Student("George", 25, 9.1, university.id)
# session.add(student1)
# session.add(student2)
# session.commit()

discipline1 = Discipline(name='Mathematics')
discipline2 = Discipline(name='Physics')
discipline3 = Discipline(name='Computer Science')

# Associate students with disciplines
student1.disciplines.extend([discipline1, discipline2])
student2.disciplines.extend([discipline2, discipline3])
student3.disciplines.append(discipline3)

# session.add_all([student1, student2, student3, discipline1, discipline2, discipline3])
session.commit()

physics_students = session.query(Student).join(Student.disciplines).filter(Discipline.name == 'Physics').all()

for student in physics_students:
    print(f"Student ID: {student.id}, Name: {student.name}")

session.close()

students = session.query(Student).all()
print(students)

graduated_students = session.query(Student).filter(Student.grade > 9.4)
for s in graduated_students:
    print(s)

some_students = session.query(Student).filter(Student.name.like("%oh%"))
for s in some_students:
    print(s)

print("------------------")
students = session.query(Student, University).filter(Student.university == University.id).\
    filter(University.name == "Harvard")
for s in students:
    print(s)

# Школа с классами
class School:
    name = ''
    classrooms = []

    def __init__(self, name="Unnamed"):
        self.name = name
        self.classrooms = []

    def __str__(self):
        return f"School: {self.name}"

    def add_classrooms(self, *classrooms):
        for room in classrooms:
            self.classrooms.append(room)


# Класс с учениками
class ClassRoom:
    number = 0
    character = ''
    students = []
    teachers = []

    def __init__(self, value: str):
        self.number, self.character = int(value[0]), value[1]
        self.students = []
        self.teachers = []

    def __str__(self):
        return f"Class: {self.number}{self.character}"

    def __repr__(self):
        return self.__str__()

    def add_student(self, student):
        self.students.append(student)
        student.classroom = self


# Предмет с преподавателем
class Subject:
    name = ''
    __teacher = None

    def __init__(self, name="Unnamed"):
        self.name = name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        self.__teacher = teacher
        teacher.subject = self

    def __str__(self):
        return f"Subject: {self.name}, teacher: {self.teacher}"

    def __repr__(self):
        return self.__str__()


# Базовый класс человека
class Person:
    firstname = ''
    lastname = ''

    def __init__(self, f_name, l_name):
        self.firstname = f_name
        self.lastname = l_name

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

    def __repr__(self):
        return self.__str__()


# Преподаватель с предметами и классами
class Teacher(Person):
    subject = None
    classrooms = []

    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.classrooms = []


# Родитель и ребенок (студент)
class Parent(Person):
    child = None


# Студент с родителями, классом
class Student(Person):
    __father, __mother = None, None
    classroom = None

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, parent: Parent):
        self.__father = parent
        parent.child = self

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, parent: Parent):
        self.__mother = parent
        parent.child = self

    def set_parents(self, father: Parent, mother: Parent):
        self.father = father
        self.mother = mother

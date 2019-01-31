from normal import *

# Create school object
school = School('MSU')  # ; print(school)

# Create some classes
class1 = ClassRoom('1A')  # ; print(class1)
class2 = ClassRoom('2A')  # ; print(class2)
class3 = ClassRoom('3A')  # ; print(class3)

school.add_classrooms(class1, class2, class3)  # ; print('School:', *school.classrooms)

# Create some teachers
teacher_one = Teacher('One', 'Teacher')  # ; print(teacher_one)
teacher_two = Teacher('Two', 'Teacher')  # ; print(teacher_two)

# Create some subjects
subject_mathematics = Subject('Mathematics')
subject_mathematics.teacher = teacher_one

subject_programming = Subject('Programming')
subject_programming.teacher = teacher_two

class1.teachers.append(teacher_one)
class1.teachers.append(teacher_two)
class2.teachers.append(teacher_two)
class3.teachers.append(teacher_one)

# Create some students
student1 = Student('Student', 'First')
student2 = Student('Student', 'Second')

parent1 = Parent('Father', 'First')
parent2 = Parent('Mother', 'First')

parent3 = Parent('Father', 'Second')
parent4 = Parent('Mother', 'Second')

student1.set_parents(parent1, parent2)
student2.set_parents(parent3, parent4)

class2.add_student(student1)
class2.add_student(student2)

# Task solution (final)

# 1. get all classes in school
all_classes = school.classrooms
print("1. All classes in school: ", all_classes)

# 2. get all students from selected class
class_students = class2.students
print("2. All students by class: ")
for x in class_students:
    print("\t", x)

# 3. get all subject of student
student_subjects = [teacher_temp.subject for teacher_temp in student2.classroom.teachers]
print("3. Subjects of student: ", student_subjects)

# 4. get names of student's parents
parents_names = [student2.father, student2.mother]
print("4. Student parents: ", parents_names)

# 5. get all teachers by class
class_teachers = class2.teachers
print("5. All teachers by class: ", class_teachers)

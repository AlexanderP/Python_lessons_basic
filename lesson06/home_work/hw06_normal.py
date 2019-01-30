# Задание-1:
# Реализуйте описанную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School(object):

    def __init__(self, name):
        self.name_school = name
        self.class_school = {}
        self.student_school = {}
        self.teacher_school = {}

    def add_student(self, lname, fname, mname, class_sh, father, mom):
        if not self.class_school.get(class_sh):
            self.class_school[class_sh] = {}
        if not self.class_school[class_sh].get('student'):
            self.class_school[class_sh]['student'] = []
        self.class_school[class_sh]['student'] += [[fname, mname, lname]]
        short = fname[0] + '.' + mname[0] + '. ' + lname
        self.student_school[short] = {
            'class_sh': class_sh,
            'parents': [father, mom]
        }

    def add_teacher(self, lname, fname, mname, subject, *classes):
        short = fname[0] + '.' + mname[0] + '. ' + lname
        if not self.teacher_school.get(short):
            self.teacher_school[short] = {
                'name': [fname, lname, mname],
                'subject': subject,
                'classes': list(classes)
            }
            for _class_sh in classes:
                if not self.class_school.get(_class_sh):
                    self.class_school[_class_sh] = {}
                if not self.class_school[_class_sh].get('subject'):
                    self.class_school[_class_sh]['subject'] = {}
                if not self.class_school[_class_sh]['subject'].get(subject):
                    self.class_school[_class_sh]['subject'][subject] = short
                else:
                    print(f'У класса {_class_sh} уже указан учитель {subject}')
        else:
            print('Данный учитель уже есть в базе')

    @property
    def get_classes(self):
        return (f'{self.name_school}\n' +
                '№\tКлассы:\n' +
                '\n'.join(f'{x + 1}.\t{y}' for x, y in
                          enumerate(self.class_school.keys())))

    def get_students(self, classes):
        if self.class_school.get(classes):
            students = []
            for _st in self.class_school[classes]['student']:
                short = _st[0][0] + '.' + _st[1][0] + '. ' + _st[2]
                students.append(short)
            return ('Список учеников:\n' + '\n'.join(f'{x + 1}.\t{y}'
                                                     for x, y in
                                                     enumerate(students)))
        else:
            return 'Данного класса нет в школе'

    def get_subject(self, name):
        if self.student_school.get(name):
            class_sh = self.student_school[name]['class_sh']
            text = f'Предметы ученика - {name}\nНазвание\t-\tУчитель'
            for key, _sub in self.class_school[class_sh]['subject'].items():
                text += f'\n{key}\t-\t{_sub}'
            return text
        else:
            return 'Данного ученика нет в школе'

    def get_parents(self, name):
        if self.student_school.get(name):
            parent = self.student_school[name]['parents']
            class_sh = self.student_school[name]['class_sh']
            return f'Родители ученика {name} - {parent[0]} и {parent[1]}'

        else:
            return 'Данного ученика нет в школе'

    def get_teacher(self, class_sh):
        if self.class_school.get(class_sh):
            text = f'Преподаватели класса - {class_sh}\nУчитель\t-\tНазвание'
            for key, _sub in  self.class_school[class_sh]['subject'].items():
                text += f'\n{_sub}\t-\t{key}'
            return text
        else:
            return 'Данного класса нет в школе'


test = School('Школа №1')
test.add_student("Селиванов", "Иларион", "Кондратович", "5А", "А.М. Селиванова", "К.А. Селиванов")
test.add_student("Вершинин", "Аскольд", "Тихонович", "5А", "В.Ф. Вершинина", "Т.В. Вершинин")
test.add_student("Уваров", "Наум", "Андроникович", "5Б", "П.В. Уварова", "А.И. Уваров")
test.add_student("Целобанов", "Казимир", "Олегович", "5Б", "Л.М. Целобанова", "О.Д. Целобанов")
test.add_student("Элькин", "Всеслав", "Мечиславович", "5В", "Д.В. Элькина", "М.В. Элькин")
test.add_student("Кудов", "Аким", "Арсениевич", "5В", "К.А. Кудова", "А.Ф. Кудов")
test.add_student("Елешев", "Матвей", "Кондратович", "5В", "А.В. Елешева", "К.В. Елешев")
test.add_student("Пишенин", "Леондий", "Феоктистович", "5В", "А.А. Пишенина", "Ф.А. Пишенин")
test.add_student("Антипов", "Ипполит", "Онуфриевич", "5А", "Ф.А. Антипова", "О.Ф. Антипов")
test.add_student("Сиянковская", "Владлена", "Мартыновна", "5В", "В.А. Сиянковская", "М.В. Сиянковский")
test.add_student("Полушина", "Ираида", "Мстиславовна", "5Б", "А.П. Полушина", "М.В. Полушин")
test.add_student("Бенедиктова", "Каролина", "Фомевна", "5А", "А.Ф. Бенедиктова", "Ф.А. Бенедиктов")
test.add_student("Скоробогатова", "Агафья", "Ильевна", "5А", "Ф.А. Скоробогатова", "И.Ф. Скоробогатов")
test.add_student("Решетова", "Надежда", "Радионовна", "5Б", "Н.П. Решетова", "Р.А. Решетов")
test.add_student("Булка", "Эдуард", "Елисеевич", "5Б", "В.Ф. Булка", "Е.А. Булка")

test.add_teacher("Болотникова", "Татьяна", "Святославовна", "Математика", "5А", "5В")
test.add_teacher("Дуболадова", "Марфа", "Елисеевна", "Математика", "5Б")
test.add_teacher("Турышева", "Инна", "Феодосьевна", "История", "5Б", "5В")
test.add_teacher("Поникарова", "Роза", "Прохоровна", "История", "5А")
test.add_teacher("Мухортова", "Владлена", "Потаповна", "Русский Язык", "5В")
test.add_teacher("Ожогина", "Каролина", "Анатолиевна", "Русский Язык", "5А", "5Б")
test.add_teacher("Бегичева", "Валерия", "Артемовна", "Литература", "5А", "5Б", "5В")
test.add_teacher("Маслюк", "Василиса", "Евсеевна", "Культура", "5А", "5В")
test.add_teacher("Блатова", "Анисья", "Игнатьеивна", "Культура", "5Б")
test.add_teacher("Гольдина", "Лиана", "Федотовна", "Иностранный язык", "5А", "5Б", "5В")
test.add_teacher("Кабаев", "Моисей", "Ильевич", "Физкультура", "5Б", "5В")
test.add_teacher("Квятковский", "Адриан", "Яковович", "Физкультура", "5А")

#print(test.name_school)
print(test.class_school)
#print(test.student_school)
#print(test.teacher_school)

print(test.get_classes)
print(test.get_students('5А'))
print()
print(test.get_students('5Б'))
print()
print(test.get_students('5В'))
print()
print(test.get_students('6А'))
print()
print(test.get_subject('А.А. Кудов'))
print()
print(test.get_subject('И.М. Полушина'))
print()
print(test.get_subject('A.М. Иванова'))
print()
print(test.get_parents('В.М. Элькин'))
print(test.get_parents('И.М. Полушина'))
print(test.get_parents('И.К. Селиванов'))
print(test.get_parents('И.К. Сидорова'))
print()
print(test.get_teacher('5А'))
print()
print(test.get_teacher('5Б'))
print()
print(test.get_teacher('5В'))
print()
print(test.get_teacher('6А'))
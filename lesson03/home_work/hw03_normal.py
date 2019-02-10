__author__ = 'Поздняков Александр Алексеевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('Задание №1')
def fibonacci(n, m):
    list = [0, 1]
    for i in range(2, m + 1):
        list += [list[i - 1] + list[i - 2]]
    return list[n:m + 1]

a, b = input('Введите 2 числа[8 10]: ').split()
print(fibonacci(int(a), int(b)))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('Задание №2')
my_list = input('Введите список для сортировки[8 10 4 3 6 8]: ').split()
def sort_to_max(origin_list):
    tmp_list = origin_list.copy()
    lenght = len(tmp_list)
    j = lenght
    n = 0
    while n < lenght:
        for i in range(1, j):
            a = tmp_list[i - 1]
            b = tmp_list[i]
            if str(a).isdigit() and str(b).isdigit():
                if float(a) > float(b):
                    tmp_list[i] = a
                    tmp_list[i - 1] = b
            else:
                if str(a) > str(b):
                    tmp_list[i] = a
                    tmp_list[i - 1] = b
        j -= 1
        n += 1
    return tmp_list

print(sort_to_max(my_list))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('Задание №3')


def my_filter(function, origin_list):
    tmp_list = []
    for i in origin_list:
        if function(i):
            tmp_list.append(i)
    return tmp_list


def my_func(x):
    return x % 2 == 0


print(my_filter(my_func, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

print('Задание №4')
xy = []
xy += [[float(i) for i in input('Введите координаты первой точки: ').split()]]
xy += [[float(i) for i in input('Введите координаты второй точки: ').split()]]
xy += [[float(i) for i in input('Введите координаты третьей точки: ').split()]]
xy += [[float(i) for i in input('Введите координаты четвертой точки: ').split()]]


def paralelogram(abcd):
    # abcd = [[2,4],[-3,7],[-6,6],[-1,3]]
    def my_length(x1, x2):
        return math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2)

    ab = my_length(abcd[0], abcd[1])
    cd = my_length(abcd[2], abcd[3])
    bc = my_length(abcd[1], abcd[2])
    da = my_length(abcd[3], abcd[0])
    ac = my_length(abcd[0], abcd[2])
    bd = my_length(abcd[1], abcd[3])
    if ab == cd and bc == da and ab != 0 and cd != 0 and bc != 0 and da != 0:
        if ac ** 2 + bd ** 2 == 2 * (ab * cd + bc * da):
            return True
    return False


print(paralelogram(xy))

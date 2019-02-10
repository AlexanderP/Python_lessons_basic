__author__ = 'Поздняков Александр Алексеевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

print('Задача №1. Решение №1')
number = abs(int(input('Введите число: ')))
while True:
    print(number % 10)
    number = number // 10
    if number == 0:
        break


print('Задача №1. Решение №2')
number = abs(int(input('Введите число: ')))
for i in str(number):
        print(i)

print('Задача №1. Решение №3')
number = abs(int(input('Введите число: ')))
i = 0
while i < len(str(number)):
    print(str(number)[i])
    i += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print('Задача №2. Решение 1.')
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
a, b = b, a
print(f'A = {a}')
print(f'B = {b}')

print('Задача №2. Решение 2.')
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
a = a + b
b = a - b
a = a - b
print(f'A = {a}')
print(f'B = {b}')


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('Задача №3')
age = int(input('Сколько Вам лет: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

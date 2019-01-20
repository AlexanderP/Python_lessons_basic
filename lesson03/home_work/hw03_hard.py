__author__ = 'Поздняков Александр Алексеевич'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print('Задание №1')
#наименьший общий делитель
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(a % b, b)
    elif b >= a:
        return gcd(a, b % a)


def fraction(arg1, arg2, func):
    if len(arg1.split('/')) == 1:
        arg1 += '/1'
    if len(arg2.split('/')) == 1:
        arg2 += '/1'
    arg1 = arg1.split()
    arg2 = arg2.split()
    arg1[-1] = arg1[-1].split('/')
    arg2[-1] = arg2[-1].split('/')
    if type(arg1[0]) == str:
        arg1[1][0] = int(arg1[1][0]) + int(arg1[1][1]) * abs(int(arg1[0]))
        if int(arg1[0]) < 0:
            arg1[1][0] *= -1
    if type(arg2[0]) == str:
        arg2[1][0] = int(arg2[1][0]) + int(arg2[1][1]) * abs(int(arg2[0]))
        if int(arg2[0]) < 0:
            arg2[1][0] *= -1
    if arg1[-1][1] != arg2[-1][1]:
        tmp_1 = int(arg1[-1][1])
        tmp_2 = int(arg2[-1][1])
        arg1[-1][0] = int(arg1[-1][0]) * tmp_2
        arg1[-1][1] = int(arg1[-1][1]) * tmp_2
        arg2[-1][1] = int(arg2[-1][1]) * tmp_1
        arg2[-1][0] = int(arg2[-1][0]) * tmp_1
    if func == 'sum':
        tmp_result = [int(arg1[-1][0]) + int(arg2[-1][0]), int(arg2[-1][1])]
    else:
        tmp_result = [int(arg1[-1][0]) - int(arg2[-1][0]), int(arg2[-1][1])]
    result = ''
    if tmp_result[0] == 0:
        return 0
    if tmp_result[0] < 0:
        result += '-'
    if abs(tmp_result[0]) // tmp_result[1] != 0:
        result += str(abs(tmp_result[0]) // tmp_result[1]) + ' '
        tmp_result[0] = abs(tmp_result[0]) % tmp_result[1]
    if tmp_result[0] != 0:
        tmp_gcd = gcd(tmp_result[0], tmp_result[1])
        result += f'{int(tmp_result[0] / tmp_gcd)}/'
        result += f'{int(tmp_result[1] / tmp_gcd)}'
    return result

n = input("Введите выражение[Например: 1/2 + 1/2 или 5/3 - 2 1/6]: ")
if n.count('+'):
    arg1, arg2 = n.replace(' + ', '+').split('+')
    print(fraction(arg1, arg2, 'sum'))
else:
    arg1, arg2 = n.split(' - ')
    print(fraction(arg1, arg2, 'sub'))
print()

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за каждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os.path
print('Задание №2')
workers_list = []
with open(os.path.join('data','workers')) as workers:
    workers_file = workers.read()
    tmp_list = workers_file.splitlines()
    for i in tmp_list[1:]:
        name, last_name, cash, post, plan = i.split()
        workers_list += [{'name': name, 'last_name': last_name, 'cash': cash,
                          'post': post, 'plan': plan}]

with open(os.path.join('data','hours_of')) as hours_of:
    hours_of_file = hours_of.read()
    tmp_list = hours_of_file.splitlines()
    for i in tmp_list[1:]:
        name, last_name, fact = i.split()
        for j in workers_list:
            if j['name'] == name and j['last_name'] == last_name:
                j['fact'] = fact

for i in workers_list:
    if int(i['plan']) > int(i['fact']):
        fact_cash = round((int(i['cash']) / int(i['plan'])) * int(i['fact']), 2)
        print(f"{i['name']} {i['last_name']} получит {fact_cash} рублей")

    elif int(i['plan']) == int(i['fact']):
        print(f"{i['name']} {i['last_name']} получит {i['cash']} рублей")
    else:
        hour_cash = int(i['cash']) / int(i['plan'])
        hour_plus =  int(i['fact']) - int(i['plan'])
        fact_cash = round(int(i['cash']) + hour_cash * hour_plus * 2, 2)
        print(f"{i['name']} {i['last_name']} получит {fact_cash} рублей")
print()
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import re

print('Задание №3')
alphabet = list(map(chr, range(ord('А'), ord('Я') + 1)))
with open(os.path.join('data','fruits.txt')) as fruits:
    file_fruits = fruits.read()
    list_fruits = file_fruits.splitlines()
for i in alphabet:
    tmp_list = list(
        filter(lambda x: re.findall(r'^{}'.format(i), x), list_fruits))
    if len(tmp_list) != 0:
        with open(os.path.join('data',f'fruits_{i}.txt'), 'w') as file:
            file.write('\n'.join(tmp_list))
print('Файлы сформированы')
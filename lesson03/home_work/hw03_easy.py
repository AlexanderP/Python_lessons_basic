__author__ = 'Поздняков Александр Алексеевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('Задание №1')
def my_round(number, ndigits):
    ints, digits = str(number).split('.')
    digits = [int(i) for i in digits]
    ints = int(ints)
    if len(digits) < ndigits:
        return number
    elif ndigits == 0:
        if int(digits[0]) >= 5:
            if ints < 0:
                ints -= 1
            else:
                ints += 1
        return ints
    else:
        if int(digits[ndigits]) >= 5:
            digits[ndigits-1] += 1
            n = ndigits - 1
            while n >= 0:
                if digits[n] == 10:
                    digits[n] = 0
                    if n != 0:
                        digits[n-1] += 1
                    else:
                        if ints < 0:
                            ints -= 1
                        else:
                            ints += 1
                else:
                    break
                n -= 1
        digits = [str(i) for i in digits]
        return str(ints) + '.' + ''.join(digits[:ndigits])

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(-2.1234567, 5))
print(my_round(-2.1999967, 5))
print(my_round(-2.9999967, 5))
print(my_round(2.9999967, 0))
print(my_round(-2.9999967, 0))
print(my_round(-2.1199967, 1))
print()

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print('Задание №2')
def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        int_list = [int(i) for i in str(ticket_number)]
        if sum(int_list[:3]) == sum(int_list[3:]):
            return True
    return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

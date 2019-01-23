import re

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
print("Задача №1")
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
print([[matrix[i][j] for i in range(3)] for j in range(3)])

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:

number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
number = ''.join(number.split())
number_2 = '41927216751987591234678962159123452612675547891957951223456672459'
print()
print("Задача №2")


def my_comp(number):
    patterns = [r"56789", r"45678", r"34567", r"23456", r"12345", r"01234",
                r"90123", r"89012", r"78901", r"67890"]
    for p in patterns:
        if re.search(p, number):
            i = re.search(p, number)
            comp = int(p[0])*int(p[1])*int(p[2])*int(p[3])*int(p[4])
            print(f'Найденно пять последовательных(максимальных) чисел'
                  f' "{p}" с индекса {i.start()} '
                  f'произведение равно {comp}')
            return True
    print("В заданом числе нет пяти последовательных чисел")
    return False


my_comp(number)
my_comp(number_2)


# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

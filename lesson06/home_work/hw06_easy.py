# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


def my_length(x1, x2):
    return math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2)


class Triangle(object):
    A: list
    B: list
    C: list
    AB: float
    BC: float
    CA: float

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.AB = my_length(self.A, self.B)
        self.BC = my_length(self.B, self.C)
        self.CA = my_length(self.C, self.A)
        self.perimeter_main = None
        self.altitude_main = None
        # проверка лежат ли точки на одной прямой
        if (A[0] - B[0]) * (C[1] - B[1]) == (C[0] - B[0]) * (A[1] - B[1]):
            self.not_triangle = True
        else:
            self.not_triangle = False

    @property
    def perimeter(self):
        if self.not_triangle:
            return 'Точки лежат на одной прямой'
        self.perimeter_main = self.AB + self.BC + self.CA
        return f'Периметр треугольника: {round(self.perimeter_main, 2)}'

    @property
    def altitude(self):
        if self.not_triangle:
            return 'Точки лежат на одной прямой'
        if self.perimeter_main is None:
            self.perimeter
        p = self.perimeter_main / 2
        self.altitude_main = (2 / self.CA) * math.sqrt(
            p * (p - self.AB) * (p - self.CA) * (p - self.BC))
        return f'Высота треугольника: {round(self.altitude_main, 2)}'

    @property
    def area(self):
        if self.not_triangle:
            return 'Точки лежат на одной прямой'
        if self.altitude_main is None:
            self.altitude
        self.area_main = (self.CA * self.altitude_main) / 2
        return f'Площадь треугольника: {round(self.area_main, 2)}'


print('Задача №1')
test = Triangle([1, 1], [2, 2], [3, 3])
print(test.perimeter)
print(test.altitude)
print(test.area)
print()
test1 = Triangle([1, 4], [22, 2], [6, 3])
print(test1.perimeter)
print(test1.altitude)
print(test1.area)
print()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium(object):
    A: list
    B: list
    C: list
    D: list
    AB: float
    BC: float
    CD: float
    DA: float

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = my_length(self.A, self.B)
        self.BC = my_length(self.B, self.C)
        self.CD = my_length(self.C, self.D)
        self.DA = my_length(self.D, self.A)
        self.perimeter_main = None
        self.altitude_main = None
        self.area_main = None
        #проверка параллельности оснований и они не равны друг другу
        if (B[1] - C[1]) / (B[0] - C[0]) == (D[1] - A[1]) / (
                D[0] - A[0]) and not self.BC == self.DA:
            self.not_trapezium = False
        else:
            self.not_trapezium = True

    @property
    def perimeter(self):
        if self.not_trapezium is True:
            return 'Заданные точки не являются вершинами трапеции'
        self.perimeter_main = self.AB + self.BC + self.CD + self.DA
        return f'Периметр трапеции: {round(self.perimeter_main, 2)}'

    @property
    def length(self):
        if self.not_trapezium is True:
            return 'Заданные точки не являются вершинами трапеции'
        return (f"Длины сторон:\n"
                f"AB = {round(self.AB, 2)}\n"
                f"BC = {round(self.BC, 2)}\n"
                f"CD = {round(self.CD, 2)}\n"
                f"DA = {round(self.DA, 2)}")

    @property
    def altitude(self):
        if self.not_trapezium is True:
            return 'Заданные точки не являются вершинами трапеции'
        d = self.DA
        a = self.AB
        b = self.BC
        c = self.CD
        self.altitude_main = math.sqrt(a ** 2 - (
                ((d - b) ** 2 + a ** 2 - c ** 2) / (2 * (d - b))) ** 2)
        return f'Высота трапеции: {round(self.altitude_main, 2)}'

    @property
    def area(self):
        if self.not_trapezium is True:
            return 'Заданные точки не являются вершинами трапеции'
        if self.altitude_main is None:
            self.altitude
        self.area_main = ((self.BC + self.DA) / 2) * self.altitude_main
        return f'Площадь трапеции: {round(self.area_main, 2)}'

    @property
    def isosceles(self):
        if self.not_trapezium is True:
            return 'Заданные точки не являются вершинами трапеции'
        if self.AB == self.CD:
            return 'Трапеция является равнобедренной'
        return 'Трапеция не является равнобедренной'


print('Задача №2')
test2 = Trapezium([-2, -2], [-3, 1], [7, 7], [3, 1])
print(test2.perimeter)
print(test2.length)
print(test2.altitude)
print(test2.area)
print(test2.isosceles)
print()
test3 = Trapezium([-1, -2], [-3, 1], [7, 7], [3, 1])
print(test3.perimeter)

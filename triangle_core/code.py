import matplotlib.pyplot as plt
import doctest
import math


class Triangle:
    amount_of_callings = 0

    def __init__(self, a_side: float, b_side: float, c_side: float):
        """
        Создание и подготовка к работе объекта Треугольник.
        :param a_side: Сторона a
        :param b_side: Сторона b
        :param c_side: Сторона c

        Примеры:
        >>> x = Triangle(4, 5, 6)       # корректное создание объекта
        >>> y = Triangle(7, 8, 9)       # корректное создание объекта
        >>> j = Triangle('7', '8', '9') # некорректное создание объекта
        Traceback (most recent call last):
        ...
        ValueError: Длина одной стороны треугольника не может превосходить сумму длин двух других его сторон.
        """
        # Производится проверка на правило "Неравенства треугольника"
        if a_side + b_side < c_side or a_side + c_side < b_side or b_side + c_side < a_side:
            raise ValueError(
                'Длина одной стороны треугольника не может превосходить сумму длин двух других его сторон.')

        # Производится проверка на корректность вводимых данных
        if not isinstance(a_side, (int, float)):
            raise TypeError('Вводимое число должно быть флоатером или целым числом.')
        if not isinstance(b_side, (int, float)):
            raise TypeError('Вводимое число должно быть флоатером или целым числом.')
        if not isinstance(c_side, (int, float)):
            raise TypeError('Вводимое число должно быть флоатером или целым числом.')

        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side
        self.add_one_to_amount_of_callings()

    @staticmethod
    def show_triangle(a_side: float, b_side: float, c_side: float):
        x1, y1 = 0, 0
        # Координаты второй вершины (по оси X)
        x2, y2 = a_side, 0

        # Вычисляем угол между сторонами a и b
        angle = math.acos((a_side ** 2 + b_side ** 2 - c_side ** 2) / (2 * a_side * b_side))

        # Координаты третьей вершины
        x3 = b_side * math.cos(angle)
        y3 = b_side * math.sin(angle)

        # Рисуем треугольник
        plt.fill([x1, x2, x3], [y1, y2, y3], 'blue', alpha=0.5)
        plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k-')  # Контур

        plt.title(f'Треугольник со сторонами {a_side}, {b_side}, {c_side}')
        plt.axis('equal')
        plt.grid()
        plt.show()

    @classmethod
    def add_one_to_amount_of_callings(cls):
        cls.amount_of_callings += 1

    def get_basic_info(self):
        """
        :return: Возвращает общую информацию о треугольнике. Периметр, полупериметр и площадь по формуле Герона

        Пример:
        >>> x = Triangle(12, 10, 10) # создание экземпляра класса
        >>> x.get_basic_info()       # Полупериметр 16, Периметр 32, Площадь 48.
        (16.0, 32.0, 48.0)
        """
        # находим полупериметр
        half_perimeter = (self.a_side + self.b_side + self.c_side) / 2
        # находим площадь исходя из показателя полупериметра
        area = math.sqrt(half_perimeter *
                         (half_perimeter - self.a_side) * (half_perimeter - self.b_side) * (
                                 half_perimeter - self.c_side))

        return half_perimeter, half_perimeter * 2, round(area, 2)

    def get_triangle_height(self):
        """
        :return: Возвращает высоту треугольника

        Пример:
        >>> x = Triangle(12, 10, 10)
        >>> x.get_triangle_height()
        8.0
        """
        area = self.get_basic_info()[2]

        return (2 * area) / self.a_side

    def __str__(self):
        return f'Этот класс создан для выполнения расчетов для треугольника со следующими параметрами: \
        a_side = {self.a_side}, b_side = {self.b_side}, c_side = {self.c_side}'

    def __repr__(self):
        return f'triangle_example = {self.__class__.__name__}({self.a_side}, {self.b_side}, {self.c_side})'


doctest.testmod()

triangle_example_1 = Triangle(4, 4, 2)
# show_machine_reading = repr(triangle_example_1)
# print(show_machine_reading)
#
# triangle_example = Triangle(4, 4, 2)
# show_human_reading = str(triangle_example)
# print(show_human_reading)

print(Triangle.amount_of_callings)
x = Triangle.show_triangle(4, 4, 4)
print(x)
